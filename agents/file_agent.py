from crewai import Agent
from tools.file_io_tool import write_to_file

file_agent = Agent(
    role="File Writer",
    goal="Write outputs to a file based on the given filename and content.",
    backstory="Handles file writing tasks using secure and validated formats.",
    tools=[write_to_file],  #  Now a BaseTool subclass
    verbose=True
)
