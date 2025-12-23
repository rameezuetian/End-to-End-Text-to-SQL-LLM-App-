

# 🧠 End-to-End Text-to-SQL LLM App

A Streamlit application that converts **natural language questions** into **SQL queries** using an LLM (Google Gemini / OpenAI) and executes them on a **SQLite database**. Perfect for building **Text-to-SQL AI demos**, learning SQL, or integrating AI-assisted database querying.

---

## Features

* Convert **English questions** into SQL queries automatically
* Execute queries on a **SQLite database** (`student.db`)
* Display results in a **user-friendly Streamlit interface**
* Supports **dynamic LLM prompts** with database schema context
* Example questions supported:

  * “Show all students from Computer Science”
  * “List students with CGPA > 3.5”
  * “Who has the highest CGPA?”

---

## Tech Stack

* **Python 3.10+**
* **Streamlit** – Web interface
* **SQLite3** – Database
* **Google Gemini API / OpenAI API** – LLM for Text-to-SQL
* **dotenv** – Load API keys securely from `.env`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rameezuetian/End-to-End-Text-to-SQL-LLM-App-.git
cd End-to-End-Text-to-SQL-LLM-App-
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API key:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## Usage

Start the Streamlit app:

```bash
streamlit run app.py
```

* Enter an **English question** about the students database
* Click **Generate & Run**
* The app will display:

  * Generated SQL query
  * Query results from SQLite

---

## Database Schema

**Table: students**

| Column     | Type    | Description                 |
| ---------- | ------- | --------------------------- |
| id         | INTEGER | Primary Key, auto-increment |
| name       | TEXT    | Student name                |
| department | TEXT    | Department                  |
| semester   | INTEGER | Current semester            |
| cgpa       | REAL    | Student CGPA                |

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* [Google Gemini API](https://developers.generativeai.google/)
* [Streamlit](https://streamlit.io/)
* Tutorials and inspiration from AI & Text-to-SQL communities

---
