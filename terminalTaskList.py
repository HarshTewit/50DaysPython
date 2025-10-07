"""
Terminal Based task manager
"""

import os

TASK_FILE = "my_tasks.txt"

def load_tasks():
    tasks = []
    if (os.path.exists(TASK_FILE)):
        #Go through each line and pull out the tasks 
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text" : text, "done": status == "done"})
    return tasks #if there is a file, then return the tasks, if not, then return the empty list 

def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")

def display_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['text']}  is {'done' if task['done'] else 'not done'} \n")

def task_manager():
    tasks = load_tasks()
    while True:
        print(f"\n ------------ TASK MANAGER --------")
        print("1. Add Task.")
        print("2. View Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task.")
        print("5. Exit.")
        choice = input("Choose an option.").strip()

        match choice:
            case "1":
                new_task = input("Enter the new task.")
                tasks.append({"text": new_task, "done": False})
                save_tasks(tasks)
                print("The task has been added to your list.")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    task_no = int(input("Which task do you want to mark as completed- enter the number."))
                    if 1 <= task_no <= len(tasks):
                        tasks[task_no - 1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as done.")
                    else:
                        print("Please enter a number that is in the range.")
                except ValueError:
                    print("Please enter a valid task number.")
            case "4":
                display_tasks(tasks)
                try:
                    task_deleted = int(input("Which task do you want to delete? Enter the number."))
                    if 1 <= task_deleted <= len(tasks):
                        removed = tasks.pop(task_deleted - 1)
                    else:
                        print("Kindly enter a number in the valid range.")
                except ValueError:
                    print("Kindly enter a valid number.")
            case "5":
                print("Exiting Task Manager. Bye!")
                break
            case _:
                print("Please choose a valid option.")


                

task_manager()