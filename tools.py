from langchain.tools import tool

@tool
def read_todos():
    """
    Reads the current to-do list from todo.txt
    """
    with open("todo.txt", "r") as file:
        lines = file.readlines()
        return [
            line.strip()
            for line in lines
            if line.strip
        ]


@tool
def add_task(task: str):
    """
    Adds a new task to the to-do list.
    """
    task = task.strip()

    if task == "":
        return "Cannot add an empty task."
        
    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    i = len(tasks)+1

    with open("todo.txt", "a") as file:
        file.write(f"[{i}] " + task + '\n')

    return "Task added."



@tool
def mark_done(task_id):
    """
    Marks a to-do item as completed using its ID.
    """
    i = task_id - 1
    try:
        with open("todo.txt") as file:
            tasks = file.readlines()

        if i < 0 or i >= len(tasks):
            return "Task ID out of range"
        tasks[i] = tasks[i].rstrip() + " - Done\n"
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
            return "Task marked as done."

    except Exception as e:
        return "something went wrong: {e}"



@tool 
def remove_task(task_id):
    """
    Removes a to-do item from the todo list using its ID 
    """
    i = task_id - 1

    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        
        remaining_tasks = [tasks[j] for j in range(len(tasks)) if j != i]
        new_tasks = []
        for j in range(len(remaining_tasks)):
            strs = remaining_tasks[j].split(']')
            task = strs[-1]
            new_tasks.append(f'[{j+1}]' + task)
        
        with open("todo.txt", "w") as file:
            file.writelines(new_tasks)

        return "Task removed successfully"
    except Exception as e:
        return e



@tool
def edit_task(task_id, new_task: str):
    """
    Edits an item in todo.txt using its ID and sets it to new_task
    """

    new_task = new_task.strip()
    if new_task == "":
        return "Cannot add an empty task."
    i = task_id - 1
    try:
        with open("todo.txt", 'r') as file:
            content = file.readlines()
        
        content[i] = f"[{task_id}] {new_task + '\n'}"

        with open("todo.txt", "w") as file:
            file.writelines(content)
        
        return "Task editted successfully"
    except Exception as e:
        return e