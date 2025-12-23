import sqlite3

# Connect to database
connection = sqlite3.connect('student.db')
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    semester INTEGER,
    cgpa REAL
)
""")

# Insert sample data
cursor.executemany("""
INSERT INTO students (name, department, semester, cgpa)
VALUES (?, ?, ?, ?)
""", [
    ("Ali Ahmed", "Computer Science", 5, 3.45),
    ("Ayesha Khan", "Software Engineering", 3, 3.80),
    ("Usman Raza", "Electrical Engineering", 7, 3.10),
    ("Fatima Noor", "Computer Science", 1, 3.90),
    ("Hassan Ali", "Data Science", 6, 3.60)
])

# Commit changes
connection.commit()

# Schema info for Text-to-SQL LLM
table_info = """
Table Name: students

Columns:
- id (INTEGER, Primary Key): Unique student ID
- name (TEXT): Student name
- department (TEXT): Department name
- semester (INTEGER): Current semester
- cgpa (REAL): Student CGPA
"""

print("Database created and sample data inserted successfully.")


data = cursor.execute('''Select * From students''')
for row in data:
    print(row)


connection.commit()
connection.close()