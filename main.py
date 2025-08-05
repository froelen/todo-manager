def main():
    action= input("What do you want to do? (use help for a list of commands)\n")

    """if action not in ["help", "exit", "add", "list", "remove", "complete", "clear"]:
        print("Invalid command. Please try again.")
        main()""" # le laisser ferait vérifier au programme deux fois si l'action est valide (puisque la meme vérification est faite dans le else)

    if action == "help":
        help()
    elif action == "exit":
        print("Exiting the task manager.")
        return
    elif action == "add":
        print("functionality to add a task is not implemented yet.")
        main()
    elif action == "list":
        print("functionality to list tasks is not implemented yet.")
        main()
    elif action == "remove":
        print("functionality to remove a task is not implemented yet.")
        main()
    elif action == "complete":
        print("functionality to mark a task as complete is not implemented yet.")
        main()
    elif action == "clear":
        print("functionality to clear all tasks is not implemented yet.")
        main()
    else: #invalid command
        print("Invalid command. Please try again.")
        main()

def help():
    print("Available commands:")
    print("1. help - Show this help message")
    print("2. exit - Exit the task manager")
    print("3. add - Add a new task")
    print("4. list - List all tasks")
    print("5. remove - Remove a task")
    print("6. complete - Mark a task as complete")
    print("7. clear - Clear all tasks")

    main()


print("Task manager by froelen.") #title
main()                            #launches main function (and thus the program)