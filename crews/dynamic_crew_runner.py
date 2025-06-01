from agents.manager_agent import get_manager_agent
from crewai import Agent, Task, Crew
from utils.functions import parse_agent_specs_from_task_outputs

def run_crew(user_input):
    # Get user prompt for the objective
    # user_prompt = input("What do you want the crew to accomplish? ")

    # Get the manager agent
    manager = get_manager_agent()

    # Create the manager's planning task
    manager_task = Task(
        description=f"""
        Based on the user's objective: "{user_input}",
        design a crew of agents that can accomplish the task.

        Return a JSON list of agents with:
          - 'role': the agent's role
          - 'goal': what the agent aims to achieve
          - 'backstory': background to give the agent context
          - 'task_description': what this agent will specifically do
        """,
        agent=manager,
        expected_output="A JSON list of agent specs with keys: role, goal, backstory, task_description."
    )


    # Run the manager crew
    manager_crew = Crew(agents=[manager], tasks=[manager_task])
    manager_output = manager_crew.kickoff()

    # Access the first task output
    # print(type(manager_output.tasks_output[0]))
    for idx, t in enumerate(manager_output.tasks_output):
        raw_content = getattr(t, "raw", None)
        print(f"Task output {idx} raw content: {repr(raw_content)}")


    # Set the Agent specs
    agent_specs = parse_agent_specs_from_task_outputs(manager_output.tasks_output)


    # Instantiate agents and tasks from spec
    agents = []
    tasks = []

    for spec in agent_specs:
        agent = Agent(
            role=spec["role"],
            goal=spec["goal"],
            backstory=spec["backstory"],
            verbose=True
        )
        task = Task(
            description=spec["task_description"],
            agent=agent,
            expected_output=f"A successful completion of: {spec['task_description']}"
        )

        agents.append(agent)
        tasks.append(task)

    # Run the dynamic crew
    print("\n=== Running Your Custom Dynamic Crew ===\n")
    dynamic_crew = Crew(agents=agents, tasks=tasks)
    final_output = dynamic_crew.kickoff()

    print("\n=== Final Output ===")
    print(final_output)
