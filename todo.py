todos = []

def add_todo():
    todo = input("Enter a new Todo: ")
    todos.append(todo)
    print(f"'{todo}' has been added!")

def main():
    while True:
        print("Todo App")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Delete Todo")
        print("4. Exit")
        choice = input("choose an option: ")

        if choice == "1":
            add_todo()
        elif choice == "2":
            print("\n".join(todos) if todos else "No todos yet!")

        elif choice == "3":
            print("Feature not implemented yet.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ =="__main__":
    main()
