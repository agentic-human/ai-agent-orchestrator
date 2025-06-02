import os
import requests
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class WebSearchInput(BaseModel):
    query: str = Field(..., description="The search query to look up on the web.")

class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = "Searches the web and returns results using Google Custom Search API."
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("GOOGLE_API_KEY")
        cse_id = os.getenv("GOOGLE_CSE_ID")
        url = "https://www.googleapis.com/customsearch/v1"

        params = {
            "key": api_key,
            "cx": cse_id,
            "q": query,
            "num": 3,  # number of results
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            # Extract and return the top few snippets
            results = data.get("items", [])
            if not results:
                return "No results found."

            output = ""
            for i, item in enumerate(results, 1):
                title = item.get("title", "No title")
                snippet = item.get("snippet", "No snippet")
                link = item.get("link", "")
                output += f"{i}. {title}\n{snippet}\n{link}\n\n"

            return output.strip()

        except Exception as e:
            return f"Error during web search: {str(e)}"

web_search_tool = WebSearchTool()
