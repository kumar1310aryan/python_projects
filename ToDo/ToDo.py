def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List:")
        if not tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

       
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task by index number")
        print("3. Exit")

        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            
        elif choice == '2':
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
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")


todo_list()
