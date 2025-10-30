list = []

while True:
    print("List of tasks")
    for i, task in enumerate(list, start=1):
        print(f"{i}. {list}")

    print("\n")
    print("Options")
    print("1. Add task")
    print("2. Delete")
    print("3. Exit")

    choice = input("Please write your task: ")

    if choice == "1":
        new_task = input("Add your task: ")
        list.append(new_task)
        print(f"Added: {new_task}")

    elif choice == "2":
        num = int(input("Define task number to remove: "))
        if 1 <= num <= len(list):
            removed = list.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Try again.")