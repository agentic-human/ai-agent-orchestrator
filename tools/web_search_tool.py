# tools/web_search_tool.py

from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

# Define the input schema for the tool
class WebSearchInput(BaseModel):
    query: str = Field(..., description="The search query to look up on the web.")

# Define the web search tool
class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = "Searches the web and returns results for a given query."
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(self, query: str) -> str:
        # Simulate a web search (replace this with real search logic or API)
        return f"Simulated search results for: '{query}'"

# Create an instance of the tool to import elsewhere
web_search_tool = WebSearchTool()
