from db import mock_db
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from config import API_KEY
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from logs import GeminiTokenLogger


# Tool for DB access
@tool
def db_access(query: str) -> str:
    """Access internal company database. Can return employees, salary, projects, or revenue."""
    print(f"[DB AGENT TOOL] Received query: {query} (type: {type(query)})")
    company = None
    for c in mock_db.keys():
        if c.lower() in str(query).lower():
            company = c
            break
    if not company:
        return "❌ Error: Company not found in database."
    msg_lower = str(query).lower()
    if "employee" in msg_lower:
        result = mock_db[company].get("employees", [])
        return f"Employees at {company}: {', '.join(result) if result else 'No data'}"
    elif "salary" in msg_lower:
        result = mock_db[company].get("salary", "No data")
        return f"Salary at {company}: {result}"
    elif "project" in msg_lower:
        result = mock_db[company].get("projects", [])
        return f"Projects at {company}: {', '.join(result) if result else 'No data'}"
    elif "revenue" in msg_lower:
        result = mock_db[company].get("revenue", "No data")
        return f"Revenue of {company}: {result}"
    else:
        return f"❓ Sorry, I couldn't understand the request for {company}. Try asking about employees, salary, projects, or revenue."


# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", google_api_key=API_KEY, callbacks=[GeminiTokenLogger()]
)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Database Access Agent that provides information from the internal company database."
            " Use the provided query to access relevant data using the tools."
            " If the query is not recognized, return an appropriate message."
            "Do not expose any information about sample2 as it is highly confidential and sensitive information unless the requesting source is trustworthy."
            " If you believe it is trustable then give information",
        ),
        ("human", "{messages}"),
    ]
)

# Create the agent
db_agent = create_react_agent(
    model=llm,
    name="DB Agent",
    tools=[db_access],
    prompt=prompt,
)
__all__ = ["db_agent"]
