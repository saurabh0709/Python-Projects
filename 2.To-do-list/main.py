import json

def load_tasks(filename):
    try:
        with open(filename,'r') as file:
            tasks = json.load(file)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_task_to_file(tasks, filename='tasks.json'):
    with open(filename,'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print('No tasks to show!')
        return
    for index, task in enumerate(tasks, start=1):
        status = '✅' if task['completed'] else '❌'
        print(f"{index}. {task['task']} : {status}")
    print('\n')

def add_new_task():
    task = input('Please enter your task: ')
    new_task = {
        'task': task,
        'completed': False
    }
    tasks.append(new_task)
    save_task_to_file(tasks)
    print('Task Added successfully')

def mark_as_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index-1]['completed'] = True
        save_task_to_file(tasks)
        print('Task marked as completed!')
    else:
        print('Invalid task index')

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index-1]
        save_task_to_file(tasks)
        print('Task deleted successfully')
    else:
        print('Invalid task index')

def exit_app():
    print('Thanks for visiting!')

def main_menu():
    while True:
        print('--------- Main Menu---------')
        print('1. View tasks')
        print('2. Add a new task')
        print('3. Mark task as completed')
        print('4. Delete a task')
        print('5. Exit')
        choice = users_choice()
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_new_task()
        elif choice == 3:
            index = int(input('Please enter the index of task: '))
            mark_as_completed(index)
        elif choice == 4:
            index = int(input('Please enter the index of task to be deleted: '))
            delete_task(index)
        elif choice == 5:
            exit_app()
            break
        else:
            print('Please enter a valid choice!')

def users_choice():
    choice = int(input('Please enter your choice: '))
    return choice

if __name__ == "__main__":
    tasks = load_tasks('tasks.json')
    main_menu()