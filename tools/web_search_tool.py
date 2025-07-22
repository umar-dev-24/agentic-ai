# tools/web_search_tool.py

from duckduckgo_search import DDGS


def search_duckduckgo(query: str, max_results: int = 10) -> str:
    with DDGS() as ddgs:
        print("Searching DuckDuckGo for:", query)
        results = ddgs.text(query, max_results=max_results)
        draft = "\n\n".join([res["body"] for res in results])
        return draft
