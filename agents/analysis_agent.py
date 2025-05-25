from crewai import Agent

analysis_agent = Agent(
    role='Data Analyst',
    goal='Make sense of collected information and find key insights',
    backstory='Loves analyzing and drawing conclusions from data.',
    verbose=True
)
