import tkinter as tk
from tkinter import messagebox

# Initialize the main application
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")
root.config(bg="#222831")  # Background color

# Global variables
current_player = "X"
board = [""] * 9  # Representing the 3x3 grid

# Function to check for a win
def check_winner():
    global board
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            # Highlight the winning line
            for idx in combo:
                buttons[idx].config(bg="#32e0c4")  # Highlight with a green color
            return board[combo[0]]
    if "" not in board:
        return "Draw"
    return None

# Function to handle button clicks
def on_click(index):
    global current_player, board
    if board[index] == "" and check_winner() is None:
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled", disabledforeground="white")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s Turn", fg="white")

# Function to reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    label.config(text="Player X's Turn", fg="white")
    for button in buttons:
        button.config(text="", state="normal", bg="#393e46")

# GUI Elements
label = tk.Label(root, text="Player X's Turn", font=("Arial", 18, "bold"), bg="#222831", fg="white")
label.pack(pady=20)

frame = tk.Frame(root, bg="#222831")
frame.pack()

buttons = []
for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 20, "bold"),
        height=2,
        width=5,
        bg="#393e46",  # Default button background
        fg="white",    # Text color
        activebackground="#eeeeee",  # Button background when clicked
        activeforeground="#222831",  # Text color when clicked
        command=lambda i=i: on_click(i)
    )
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 14, "bold"),
    bg="#32e0c4",
    fg="#222831",
    activebackground="#eeeeee",
    activeforeground="#222831",
    command=reset_game
)
reset_button.pack(pady=20)

# Start the application
root.mainloop()