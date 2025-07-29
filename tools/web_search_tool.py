# tools/web_search_tool.py

from duckduckgo_search import DDGS


from duckduckgo_search import DDGS


def search_duckduckgo(query: str, max_results: int = 10) -> str:
    with DDGS() as ddgs:
        print("Searching DuckDuckGo for:", query)
        results = ddgs.text(query, max_results=max_results)
        draft_list = []
        for res in results:
            url = res.get("href", "")
            body = res.get("body", "")
            print(f"🔗 Source: {url}")
            draft_list.append(body)
        return "\n\n".join(draft_list)
