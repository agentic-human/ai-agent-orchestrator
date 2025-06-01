from dotenv import load_dotenv
load_dotenv()
from crews.static_crew_runner import run_task 
from crews.dynamic_crew_runner import run_crew

def main():
    print("Choose execution mode:")
    print("1. Use statically defined crew")
    print("2. Generate crew dynamically using manager agent")
    choice = input("Enter 1 or 2: ")

    if choice.strip() == "1":
        user_input = input("Enter a high-level research task: ")
        run_task(user_input)
    elif choice.strip() == "2":
        user_input = input("Enter a high-level research task: ")
        run_crew(user_input)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

