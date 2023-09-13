class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date, priority, category):
        try:
            # Validate due_date (you can implement more detailed validation)
            if not due_date:
                raise ValueError("Due date cannot be empty")

            # Validate priority (you can implement more detailed validation)
            if priority not in ["low", "medium", "high"]:
                raise ValueError("Invalid priority. Choose 'low', 'medium', or 'high'")

            task = {
                "title": title,
                "due_date": due_date,
                "priority": priority,
                "category": category,
            }
            self.tasks.append(task)
            print("Task added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task["title"] != title]

    def view_tasks(self):
        return self.tasks

def main():
    task_manager = TaskManager()

    while True:
        print("Task Manager Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority (low/medium/high): ")
            category = input("Enter category: ")
            task_manager.add_task(title, due_date, priority, category)
        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            task_manager.delete_task(title)
        elif choice == "3":
            tasks = task_manager.view_tasks()
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(f"Title: {task['title']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Category: {task['category']}")
            else:
                print("No tasks found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
