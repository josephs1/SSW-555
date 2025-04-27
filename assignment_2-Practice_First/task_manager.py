# Group: Joseph Stefanoni, Hala Basyouni, Shrihit Saxena, Alice Zaytseva
"""
User Story:
As a user,
I want to add, remove, and view the number of tasks and the tasks themselves in a to-do list,
So that I can manage my tasks efficiently.
"""

todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)

def view_tasks():
    return todo_list

def number_of_tasks():
    return len(todo_list)

def reset_list():
    todo_list.clear()