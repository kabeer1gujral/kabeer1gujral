import json

FILENAME = 'todo_list.json'

def load_tasks():
    try:
        with open(FILENAME, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task['done'] else "Not Done"
        print(f"{i + 1}. {task['description']} [{status}]")

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({'description': description, 'done': False})
    save_tasks(tasks)
    print("Task added successfully.")

def mark_task_done(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['done'] = True
        save_tasks(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
