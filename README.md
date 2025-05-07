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
```

- **Do not commit `config.yaml` to version control.** It is excluded via `.gitignore`.
- Edit `config.yaml` to match your MySQL credentials.

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