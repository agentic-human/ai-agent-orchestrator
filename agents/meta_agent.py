from crewai import Agent, Task
from agents.data_agent import data_agent
from agents.analysis_agent import analysis_agent
from agents.writer_agent import writer_agent

meta_agent = Agent(
    role='Meta Agent',
    goal='Oversee the creation and coordination of agents to solve tasks',
    backstory="You are a highly capable orchestrator who knows how to delegate and manage agent workflows.",
    verbose=True
)

def assign_agents(task_input):
    return [
        (data_agent, Task(
            description=f"Collect information about: {task_input}",
            expected_output="Relevant and accurate raw data or facts.",
            role="data agent",
            agent=data_agent
        )),
        (analysis_agent, Task(
            description="Analyze and summarize findings from the data.",
            expected_output="A coherent analysis with key insights.",
            role="analysis agent",
            agent=analysis_agent
        )),
        (writer_agent, Task(
            description="Generate a written report based on the analysis.",
            expected_output="A well-written summary or article based on the findings.",
            role="writer agent",
            agent=writer_agent
        ))
    ]
