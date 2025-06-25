# Task 05 : File I/O - Persistent Data Storage

class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.task_id}] {self.title} - {self.status}\n  Description: {self.description}"

    def to_line(self):
        return f"{self.task_id}|{self.title}|{self.description}|{self.status}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split("|")
        if len(parts) == 4:
            return Task(parts[0], parts[1], parts[2], parts[3])
        return None


tasks = []


def load_tasks(filename="tasks.txt"):
    tasks.clear()
    try:
        with open(filename, "r") as file:
            for line in file:
                task = Task.from_line(line)
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        open(filename, "w").close()
    except Exception as e:
        print(f"❌ Error loading tasks: {e}")


def save_tasks(filename="tasks.txt"):
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task.to_line() + "\n")
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")


def create_task():
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    task = Task(task_id, title, description)
    tasks.append(task)
    save_tasks()
    print("✅ Task created and saved!")


def read_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nList of Tasks:")
        for task in tasks:
            print(task)


def update_task():
    task_id = input("Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("New Title: ")
            task.description = input("New Description: ")
            task.status = input("New Status (Pending/Done): ")
            save_tasks()
            print("✅ Task updated and saved!")
            return
    print("❌ Task not found!")


def delete_task():
    task_id = input("Enter Task ID to delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            save_tasks()
            print("✅ Task deleted and saved!")
            return
    print("❌ Task not found!")


def main():
    load_tasks()
    while True:
        print("\n📂 Task Manager Menu:")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            create_task()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("All tasks saved to file.")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()