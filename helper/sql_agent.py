import openai
import mysql.connector
import os
import yaml
from typing import List, Dict, Any
import asyncio

# Load DB config (reuse logic from app.py)
def load_db_config():
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "config.yaml"), "r") as f:
            config = yaml.safe_load(f)
            db_cfg = config.get("database", {})
            return {
                'host': db_cfg.get('host', 'localhost'),
                'user': db_cfg.get('user', 'root'),
                'password': db_cfg.get('password', ''),
                'database': db_cfg.get('name', 'csc3170')
            }
    except Exception:
        return {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'csc3170'
        }

DB_CONFIG = load_db_config()

# Only allow schema inspection, never data modification/execution
def get_schema() -> Dict[str, Any]:
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        schema = {}
        for table in tables:
            cursor.execute(f"DESCRIBE `{table}`")
            schema[table] = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        return schema
    except Exception as e:
        return {"error": str(e)}
    finally:
        if conn:
            conn.close()

# SQL Agent for advice and warnings
class SQLAgent:
    def __init__(self, openai_api_key=None, model=None):
        self.schema = get_schema()
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        self.model = model or os.getenv("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo")
        openai.api_key = self.openai_api_key

    def _build_system_prompt(self) -> str:
        return (
            "You are a SQL advisor agent. You will be given a user request and the database schema. "
            "You must always inspect the schema first. "
            "You must never execute or modify the database, but you can inspect schema/tables. "
            "Respond with a JSON array of objects, each with 'action' (INSERT, QUERY, DELETE, UPDATE, or SCHEMA_INSPECTION) and 'command' (the SQL or schema advice). "
            "If the action is INSERT, UPDATE, or DELETE, always include a warning in your response about not executing or modifying the database. "
            "Here are some examples: "
            "\nUser: I need to delete the information of a student named John who dropped out in the class of 2021. He is French, his GPA is 1.5, his student ID is 125090833, and his major is data science.\n"
            "Response: [{\"action\": \"DELETE\", \"command\": \"DELETE FROM Student WHERE StudentID = 125090833 AND Name = 'John' AND Year = 2021 AND Nation = 'France' AND GPA = 1.5 AND Major = 'data science'\"}, {\"action\": \"WARNING\", \"command\": \"This is a DELETE operation. The agent will not execute or modify the database.\"}]\n"
            "User: Please help me find the email addresses of the students who are taking Linear Algebra taught by Tom Willson in the spring semester of 2025. The students should be in their sophomore or junior year.\n"
            "Response: [{\"action\": \"QUERY\", \"command\": \"SELECT s.`E - mail` FROM Student JOIN Course c ON s.Year = c.Year JOIN Professor p ON c.Instructor = p.InstructorID WHERE c.Year = 2024 AND c.Schedule LIKE '%Spring%' AND c.`Course Name` = 'Linear Algebra' AND p.Name = 'Tom Willson' AND (s.Year = 2 OR s.Year = 3)'\"}]\n"
            "User: add a new student named Lucy from the class of 2026, majoring in Math, belonging to ABC college, with a GPA of 3.8, and her phone number is 13800138000\n"
            "Response: [{\"action\": \"INSERT\", \"command\": \"INSERT INTO Student (StudentID, Name, E - mail, Gender, Year, Major, GPA, School, College, `Tuition fees`, Scholarships, `Financial Aids`, `Honors and Rewards`, Nation, `Phone Numbers`, `Mailing Address`, `Emergency Contact`, `Graduate Status`) VALUES (NULL, 'Lucy', 'none', 'none', 2026, 'Math', 3.8, 'none', 'ABC', 'none', 'none', 'none', 'none', 'none', '13800138000', 'none', 'none', 'none')\"}, {\"action\": \"WARNING\", \"command\": \"This is an INSERT operation. The agent will not execute or modify the database.\"}]\n"
            "User: Find all students from class 2026 with a GPA higher than 3.5\n"
            "Response: [{\"action\": \"QUERY\", \"command\": \"SELECT * FROM Student WHERE Year = 2026 AND GPA > 3.5\"}]\n"
            "User: What tables are in the database?\n"
            "Response: [{\"action\": \"SCHEMA_INSPECTION\", \"command\": \"Tables: Student, Course, Professor, ...\"}]\n"
        )

    async def aget_sql_advice(self, user_input: str) -> List[Dict[str, str]]:
        schema_info = self.schema
        system_prompt = self._build_system_prompt() + "\nThe following is the schema for the database entities and their attributes:\n" + str(schema_info)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=1024
            ))
            content = response["choices"][0]["message"]["content"]
            import json
            return json.loads(content)
        except Exception as e:
            return [{"action": "ERROR", "command": str(e)}]

# For use in custom_sql
agent_instance = SQLAgent()
def get_sql_agent_advice(user_input: str):
    return agent_instance.get_sql_advice(user_input)

async def aget_sql_agent_advice(user_input: str):
    return await agent_instance.aget_sql_advice(user_input)