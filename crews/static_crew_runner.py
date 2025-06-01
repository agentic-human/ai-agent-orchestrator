from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from agents.meta_agent import meta_agent, assign_agents

def run_task(user_input):
    # Assign agents and tasks dynamically based on the input
    task_plan = assign_agents(user_input)

    for agent, task in task_plan:
        print(f"\n--- Agent: {agent.role} ---")
        print(f"Task: {task}")
        print(f"Task description: {task.description}")
        print(f"Task type: {type(task)}")
        print(f"Task config: {getattr(task, 'config', 'NO CONFIG')}")
        print(f"Config type: {type(getattr(task, 'config', {}))}")



    # Create the crew
    crew = Crew(
        agents=[meta_agent] + [a for a, _ in task_plan],
        tasks=[t for _, t in task_plan], 
        verbose=True
    )


    # Run the crew
    result = crew.kickoff()

    # Output the final result
    print("\n--- Final Output ---\n")
    print(result)
