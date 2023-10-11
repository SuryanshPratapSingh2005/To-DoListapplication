import sys
import os
import tkinter as tk

# Command-line functions

def add_task(task):
    with open('todo.txt', 'a') as f:
        f.write(task + '\n')

def list_tasks():
    with open('todo.txt', 'r') as f:
        tasks = f.readlines()
    for task in tasks:
        print(task)

def mark_task_completed(task):
    with open('todo.txt', 'r') as f:
        tasks = f.readlines()
    with open('todo.txt', 'w') as f:
        for task_line in tasks:
            if task_line != task + '\n':
                f.write(task_line)

# GUI functions

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('To-Do List')

        # Create a listbox to display the to-do list items
        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack()

        # Create a button to add a new task to the to-do list
        self.add_task_button = tk.Button(self, text='Add Task', command=self.add_task)
        self.add_task_button.pack()

        # Create a button to mark a task as completed
        self.mark_task_completed_button = tk.Button(self, text='Mark Task Completed', command=self.mark_task_completed)
        self.mark_task_completed_button.pack()

        # Load the to-do list items from the file
        self.load_to_do_list()

    def add_task(self):
        # Get the new task to add from the user
        new_task = tk.simpledialog.askstring('Add Task', 'Enter a new task:')

        # Add the new task to the to-do list
        self.task_listbox.insert('end', new_task)

        # Save the to-do list to the file
        self.save_to_do_list()

    def mark_task_completed(self):
        # Get the index of the task to mark as completed
        selected_task_index = self.task_listbox.curselection()[0]

        # Mark the task as completed
        self.task_listbox.delete(selected_task_index)

        # Save the to-do list to the file
        self.save_to_do_list()

    def load_to_do_list(self):
        # Open the to-do list file
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()

        # Add the to-do list items to the listbox
        for task in tasks:
            self.task_listbox.insert('end', task)

    def save_to_do_list(self):
        # Open the to-do list file
        with open('todo.txt', 'w') as f:
            for task in self.task_listbox.get(0, 'end'):
                f.write(task + '\n')

# Main function

if __name__ == '__main__':
    # Check if the command-line interface is being used
    if len(sys.argv) == 1:
        # Create a GUI-based to-do list application
        todo_app = TodoListApp()
        todo_app.mainloop()
    else:
        # Handle command-line arguments
        if sys.argv[1] == 'add':
            add_task(sys.argv[2])
        elif sys.argv[1] == 'list':
            list_tasks()
        elif sys.argv[1] == 'complete':
            mark_task_completed(sys.argv[2])
        else:
            print('Usage: todo.py [add|list|complete] <task>')
