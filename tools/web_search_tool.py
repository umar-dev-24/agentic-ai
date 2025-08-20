# # tools/web_search_tool.py

# from duckduckgo_search import DDGS
# import requests


# def search_duckduckgo(query: str, max_results: int = 10) -> str:
#     with DDGS() as ddgs:
#         # results = ddgs.text(query, max_results=max_results)

#         url = "http://localhost:8000/scrap.html"
#         results = requests.get(url)
#         print(results)
#         draft = "\n\n".join([res["body"] for res in results])
#         return draft
import requests


def search_duckduckgo(query: str, max_results: int = 10) -> str:
    url = "http://localhost:8000/scrap.html"
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        return f"Failed to fetch the URL: {response.status_code}"
