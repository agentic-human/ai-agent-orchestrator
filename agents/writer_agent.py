from crewai import Agent

writer_agent = Agent(
    role='Technical Writer',
    goal='Write clear and comprehensive content based on data',
    backstory='Skilled in turning analysis into high-quality written reports.',
    verbose=True
)
