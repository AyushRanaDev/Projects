import tkinter as tk
from tkinter import messagebox

# Create the main application window
def create_app():
    # Function to add a task
    def add_task():
        task = task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Input Error", "Please enter a task!")
        else:
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)

    # Function to remove the selected task
    def remove_task():
        try:
            selected_task_index = task_listbox.curselection()[0]
            task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove!")

    # Initialize the window
    window = tk.Tk()
    window.title("To-Do List")

    # Input field and Add button
    task_entry = tk.Entry(window, width=40)
    task_entry.pack(pady=10)

    add_button = tk.Button(window, text="Add Task", width=15, command=add_task)
    add_button.pack()

    # Listbox to display tasks
    task_listbox = tk.Listbox(window, width=50, height=15, selectmode=tk.SINGLE)
    task_listbox.pack(pady=10)

    # Remove button
    remove_button = tk.Button(window, text="Remove Task", width=15, command=remove_task)
    remove_button.pack(pady=5)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    create_app()