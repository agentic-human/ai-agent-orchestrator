from crewai import Agent
from tools.web_search_tool import web_search_tool

data_agent = Agent(
    role="Data Analyst",
    goal="Analyze web data and generate insights",
    backstory="An expert analyst skilled in leveraging online resources to provide timely data insights.",
    tools=[web_search_tool],
    verbose=True
)
