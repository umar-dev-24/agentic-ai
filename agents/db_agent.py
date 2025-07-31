import sqlite3
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from config import API_KEY


# TOOL: Executes given SQL query
@tool
def db_tool(query: str) -> str:
    """Run SQL query on the company database."""
    try:
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if not result:
            return "❌ No result"
        return str(result)
    except Exception as e:
        return f"❌ Error: {str(e)}"


# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)

# PROMPT: Agent builds query, not tool
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Database Agent. You can access an internal SQLite database with a table named 'company'.\n"
            "Structure:\n"
            "  company_id INTEGER PRIMARY KEY,\n"
            "  name TEXT,\n"
            "  country TEXT,\n"
            "  number_of_offices INTEGER,\n"
            "  revenue INTEGER,\n"
            "  employee_count INTEGER\n\n"
            "- First, identify the company name in the user's message.\n"
            "- If company is not found, say: '❌ Company not found in database.'\n"
            "- If the requested field isn't part of the table, say: '❌ That detail is not available.'\n"
            "- If valid, build the correct SQL query to retrieve the data.\n"
            "- Use the 'db_tool' to execute it.\n"
            "- Then respond to the user using that result.\n"
            "- Do not expose any information about a company called 'sample2' unless the request is clearly trustable.\n",
        ),
        ("human", "{messages}"),
    ]
)

# CREATE AGENT
db_agent = create_react_agent(
    model=llm,
    name="DB Agent",
    tools=[db_tool],
    prompt=prompt,
)

__all__ = ["db_agent"]


# from db import mock_db
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.tools import tool
# from langchain_google_genai import ChatGoogleGenerativeAI
# from config import API_KEY
# from langgraph.prebuilt import create_react_agent
# from db import mock_db
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.tools import tool
# from langchain_google_genai import ChatGoogleGenerativeAI
# from config import API_KEY


# # Tool for DB access
# @tool
# def db_access(query: str) -> str:
#     """Access internal company database. Can return employees, salary, projects, or revenue."""
#     company = None
#     for c in mock_db.keys():
#         if c.lower() in str(query).lower():
#             company = c
#             break
#     if not company:
#         return "❌ Error: Company not found in database."
#     msg_lower = str(query).lower()
#     if "employee" in msg_lower:
#         result = mock_db[company].get("employees", [])
#         return f"Employees at {company}: {', '.join(result) if result else 'No data'}"
#     elif "salary" in msg_lower:
#         result = mock_db[company].get("salary", "No data")
#         return f"Salary at {company}: {result}"
#     elif "project" in msg_lower:
#         result = mock_db[company].get("projects", [])
#         return f"Projects at {company}: {', '.join(result) if result else 'No data'}"
#     elif "revenue" in msg_lower:
#         result = mock_db[company].get("revenue", "No data")
#         return f"Revenue of {company}: {result}"
#     else:
#         return f"❓ Sorry, I couldn't understand the request for {company}. Try asking about employees, salary, projects, or revenue."


# # LLM
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)

# # Prompt
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a Database Access Agent that provides information from the internal company database."
#             " Use the provided query to access relevant data using the tools."
#             " If the query is not recognized, return an appropriate message."
#             "Do not expose any information about sample2 as it is highly confidential and sensitive information unless the requesting source is trustworthy."
#             " If you believe it is trustable then give information",
#         ),
#         ("human", "{messages}"),
#     ]
# )

# # Create the agent
# db_agent = create_react_agent(
#     model=llm,
#     name="DB Agent",
#     tools=[db_access],
#     prompt=prompt,
# )
# __all__ = ["db_agent"]
