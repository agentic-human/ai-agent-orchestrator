from crewai import Agent

def get_manager_agent():
    return Agent(
        role="Project Manager",
        goal="Design a team to accomplish a user-defined objective.",
        backstory="A veteran manager skilled in assembling effective AI task forces.",
        allow_delegation=False,
        verbose=True
    )
