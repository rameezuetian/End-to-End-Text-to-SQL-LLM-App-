import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables


# Configure Gemini API
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.0-flash")

# SQLite connection
connection = sqlite3.connect("student.db", check_same_thread=False)
cursor = connection.cursor()

# Table schema (LLM context)
table_info = """
Table Name: students

Columns:
- id (INTEGER, Primary Key)
- name (TEXT)
- department (TEXT)
- semester (INTEGER)
- cgpa (REAL)
"""

# Function: Convert Text → SQL using Gemini
def get_sql_query(question):
    prompt = f"""
    You are an expert SQL generator.
    Convert the following question into an SQLite query.
    Use ONLY the table provided.

    {table_info}

    Question: {question}
    SQL Query:
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Function: Execute SQL
def run_sql(sql):
    try:
        cursor.execute(sql)
        return cursor.fetchall(), cursor.description
    except Exception as e:
        return str(e), None

# Streamlit UI
st.title("🧠 Text to SQL using Gemini + SQLite")

question = st.text_input("Ask a question about students:")

if st.button("Generate SQL & Run"):
    if question:
        sql_query = get_sql_query(question)
        st.code(sql_query, language="sql")

        result, description = run_sql(sql_query)

        if isinstance(result, str):
            st.error(result)
        else:
            columns = [desc[0] for desc in description]
            st.dataframe(result, use_container_width=True)
    else:
        st.warning("Please enter a question.")
