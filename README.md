# CSC 3170 Database Web Interface

## Project Overview
This project is a web interface for managing university data using a MySQL database. It allows you to view and add students and professors, and run custom SQL queries via a Streamlit app.

## MySQL Server Setup

1. **Install MySQL Server**
   - Download and install MySQL Community Server from the [official website](https://dev.mysql.com/downloads/mysql/).
   - Follow the installation instructions for your operating system.

2. **Start MySQL Server**
   - On Windows, use the MySQL Notifier or run the MySQL service from the Services app.
   - On macOS/Linux, use the terminal: `sudo service mysql start` or `brew services start mysql`.

3. **Create the Database**
   - Open a terminal or command prompt and log in to MySQL:
     ```
     mysql -u root -p
     ```
   - Create the database:
     ```sql
     CREATE DATABASE csc3170;
     USE csc3170;
     ```

4. **Import the Schema and Data**
   - From the MySQL prompt or terminal:
     ```sql
     SOURCE path/to/schema.sql;
     SOURCE path/to/insert.sql;
     ```
   - Or, using the command line:
     ```
     mysql -u root -p csc3170 < schema.sql
     mysql -u root -p csc3170 < insert.sql
     ```

## Configuration

All database connection settings are stored in `config.yaml`:

```yaml
# config.yaml
database:
  host: localhost
  user: root
  password: ""
  name: csc3170

openai:
  api_key: "your_openai_api_key"  # OpenAI API密钥
  default_model: "gpt-3.5-turbo"  # 默认OpenAI模型
```

- **Do not commit `config.yaml` to version control.** It is excluded via `.gitignore`.
- Edit `config.yaml` to match your MySQL credentials and OpenAI API设置。

## Running the Application

1. **Install Python dependencies**
   - Ensure you have Python 3.11+ installed.
   - Install required packages:
     ```
     pip install -r requirements.txt
     ```

2. **Start the Streamlit app**
   ```
   streamlit run app.py
   ```

3. **Access the web interface**
   - Open the provided local URL in your browser (usually http://localhost:8501/).

## Notes
- Make sure MySQL server is running and the database/schema are set up before starting the app.
- If you change database credentials, update `config.yaml` accordingly.
- For any issues, check error messages in the Streamlit app or terminal.

## Foreign Key Constraints
When importing data using `insert.sql`, you may encounter foreign key constraint errors if the data insertion order is incorrect. To avoid this:

1. Always import `schema.sql` first to create tables with foreign key relationships
2. When importing data, ensure referenced records exist before inserting dependent records
3. If needed, temporarily disable foreign key checks during import:
   ```sql
   SET FOREIGN_KEY_CHECKS=0;
   SOURCE path/to/insert.sql;
   SET FOREIGN_KEY_CHECKS=1;
   ```
4. Alternatively, modify `insert.sql` to ensure proper insertion order

## Acknowledgments

We would like to extend our sincere gratitude to `https://github.com/gbasin` and all the contributors of the `https://github.com/gbasin/LLM-DB` project. The LLM helper in our project is inspired by and references the code from their repository. Their excellent work and dedication to open-source have provided us with a valuable starting point and a wealth of inspiration.

The open-source spirit demonstrated by the `https://github.com/gbasin/LLM-DB` project has not only accelerated the development process of our project but also enhanced the overall quality of our code. We believe that the open-source community is a powerful force for innovation, and we are honored to be part of this ecosystem.

If you are interested in learning more about the original project, please visit `https://github.com/gbasin/LLM-DB` on GitHub.

## LLM helper
We use historical data to enable the model to respond and execute operations quickly. Here are examples of four basic operations: insert, delete, query, and update. LLM only provides SQL statements, and delete and update operations will go through three rounds of review to prevent incorrect operations from causing detrimental chain reactions in the database.