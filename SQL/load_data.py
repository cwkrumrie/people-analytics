import sqlite3
import pandas as pd
import os

print("Looking for files in:", os.getcwd())

# Create database file

conn = sqlite3.connect("SQL\open_university.db")

# List of CSV files and table names.

files = {
    "SQL\studentInfo.csv": "studentInfo",
    "SQL\studentAssessment.csv": "studentAssessment",
    "SQL\studentRegistration.csv": "studentRegistration",
    "SQL\studentVle.csv": "studentVle",
    "SQL\\assessments.csv": "assessments",
    "SQL\courses.csv": "courses",
    "SQL\\vle.csv": "vle"    
}

# Loop through files and load into SQLite
for filename, tablename in files.items():
    print(f"Loading {filename} into table '{tablename}'...")
    try:
        df = pd.read_csv(filename)
        df.to_sql(tablename, conn, if_exists="replace", index=False)
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")

# See what tables were created
print("\n✅ Data load complete. Tables in database:")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

conn.close()