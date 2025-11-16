FILENAME = "task.txt"  # имя файла для хранения задач


def load_tasks():
    """Загрузить список задач из файла. Вернуть список строк (без '\n')."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            # strip() убирает перенос строки и возможные пробелы
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        # Если файла нет — начинаем с пустого списка
        return []


def save_tasks(tasks):
    """Записать текущий список задач в файл, по одной задаче на строку."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")


def main():
    tasks = load_tasks()  # загрузили задачи при старте

    while True:
        print("\nList of tasks:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")  # печатаем конкретную задачу
        else:
            print(" (no tasks)")

        print("\nOptions")
        print("1. Add task")
        print("2. Delete task")
        print("3. Exit")

        choice = input("Choose option (1/2/3): ").strip()

        if choice == "1":
            new_task = input("Add your task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)  # сохраняем сразу после изменения
                print(f"Added: {new_task}")
            else:
                print("Empty task not added.")

        elif choice == "2":
            if not tasks:
                print("No tasks to delete.")
                continue

            num_str = input("Define task number to remove: ").strip()
            try:
                num = int(num_str)
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)  # сохраняем после удаления
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Try again.")


if __name__ == "__main__":
    main()


# ---------------
