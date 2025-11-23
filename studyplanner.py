import numpy as np

tasks = np.array([], dtype=str)

while True:
    print("\n--- STUDY PLANNER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks = np.append(tasks, task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        print("Thank you for using study planner!")
        break

    else:
        print("Invalid choice. Try again.")
