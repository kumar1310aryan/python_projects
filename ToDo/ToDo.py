def todo_list():
    tasks = []

    while True:
        # Display the to-do list
        print("\nTo-Do List:")
        if not tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        # Display the options
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task by index number")
        print("3. Exit")

        # Get user's choice
        choice = input("Choose an option: ")

        if choice == '1':
            # Add a new task
            task = input("Enter a new task: ")
            tasks.append(task)
        elif choice == '2':
            # Remove a task by its index number
            try:
                task_number = int(input("Enter task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    tasks.pop(task_number - 1)
                    print(f"Task {task_number} has been removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            # Exit the application
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the to-do list application
todo_list()
