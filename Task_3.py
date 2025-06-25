class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.task_id}] {self.title} - {self.status}\n  Description: {self.description}"


tasks = []

def create_task():
    task_id = input(" Enter Task ID: ")
    title = input(" Enter Task Title: ")
    description = input(" Enter Task Description: ")
    task = Task(task_id, title, description)
    tasks.append(task)
    print("✅ Task created successfully!")

def read_tasks():
    if not tasks:
        print(" No tasks available.")
    else:
        print("\n List of Tasks:")
        for task in tasks:
            print(task)

def update_task():
    task_id = input(" Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.title = input(" New Title: ")
            task.description = input(" New Description: ")
            task.status = input("New Status (Pending/Done): ")
            print("✅ Task updated successfully!")
            return
    print("❌ Task not found!")

def delete_task():
    task_id = input(" Enter Task ID to delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("✅ Task deleted successfully!")
            return
    print("❌ Task not found!")

def main():
    while True:
        print("\n📂 Task Manager Menu:")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input(" Enter your choice (1–5): ")

        if choice == "1":
            create_task()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(" Exiting Task Manager. Bye bye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
