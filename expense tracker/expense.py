import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize an empty DataFrame to store expenses
expenses_df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

def add_expense(date, category, description, amount):
    """
    Add a new expense to the DataFrame.
    """
    global expenses_df
    new_expense = pd.DataFrame([[date, category, description, amount]], columns=["Date", "Category", "Description", "Amount"])
    expenses_df = pd.concat([expenses_df, new_expense], ignore_index=True)

def view_expenses():
    """
    Return all expenses.
    """
    global expenses_df
    return expenses_df

def generate_report():
    """
    Generate and return a report grouped by category.
    """
    global expenses_df
    report = expenses_df.groupby("Category").sum()
    return report

def save_expenses(file_name="expenses.csv"):
    """
    Save the expenses DataFrame to a CSV file.
    """
    global expenses_df
    expenses_df.to_csv(file_name, index=False)

def load_expenses(file_name="expenses.csv"):
    """
    Load expenses from a CSV file into the DataFrame.
    """
    global expenses_df
    expenses_df = pd.read_csv(file_name)

def add_expense_gui():
    date = entry_date.get()
    category = entry_category.get()
    description = entry_description.get()
    try:
        amount = float(entry_amount.get())
        add_expense(date, category, description, amount)
        messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a number.")

def view_expenses_gui():
    expenses = view_expenses()
    text_expenses.delete("1.0", tk.END)
    text_expenses.insert(tk.END, expenses.to_string(index=False))

def generate_report_gui():
    report = generate_report()
    text_report.delete("1.0", tk.END)
    text_report.insert(tk.END, report.to_string())

def save_expenses_gui():
    file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_name:
        save_expenses(file_name)
        messagebox.showinfo("Success", f"Expenses saved to {file_name}")

def load_expenses_gui():
    file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_name:
        load_expenses(file_name)
        messagebox.showinfo("Success", f"Expenses loaded from {file_name}")

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker")

# Create and place the input fields and labels
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Category:").grid(row=1, column=0, padx=10, pady=5)
entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=5)
entry_description = tk.Entry(root)
entry_description.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=3, column=0, padx=10, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=3, column=1, padx=10, pady=5)

# Create and place the buttons
tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="View Expenses", command=view_expenses_gui).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Generate Report", command=generate_report_gui).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save Expenses", command=save_expenses_gui).grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(root, text="Load Expenses", command=load_expenses_gui).grid(row=8, column=0, columnspan=2, pady=10)

# Create and place the text boxes for displaying expenses and reports
text_expenses = tk.Text(root, height=10, width=50)
text_expenses.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

text_report = tk.Text(root, height=10, width=50)
text_report.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
