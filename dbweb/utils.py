import mysql.connector
from mysql.connector import Error
import yaml
import logging
import os
import streamlit as st

def load_db_config():
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
            db_cfg = config.get("database", {})
            return {
                'host': db_cfg.get('host', 'localhost'),
                'user': db_cfg.get('user', 'root'),
                'password': db_cfg.get('password', ''),
                'database': db_cfg.get('name', 'csc3170')
            }
    except Exception as e:
        st.error(f"Failed to load database config: {e}")
        logging.error(f"Failed to load database config: {e}")
        return {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'csc3170'
        }

DB_CONFIG = load_db_config()

if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        logging.error(f"Error connecting to MySQL: {e}")
        return None

def run_query(query, params=None):
    conn = get_connection()
    if conn is None:
        logging.error("No database connection available.")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        if query.strip().lower().startswith('select'):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = cursor.rowcount
        cursor.close()
        conn.close()
        logging.info(f"Executed query: {query} | Params: {params}")
        return result
    except Error as e:
        st.error(f"Query failed: {e}")
        logging.error(f"Query failed: {e} | Query: {query} | Params: {params}")
        return None