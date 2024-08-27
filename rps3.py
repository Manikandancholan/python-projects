import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        return "user"
    else:
        return "computer"

def start_game():
    global total_rounds, user_score, computer_score, current_round
    
    try:
        total_rounds = int(round_entry.get())
        if total_rounds <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the number of rounds.")
        return

    user_score = 0
    computer_score = 0
    current_round = 0

    round_text.set(f"Round: {current_round}/{total_rounds}")
    result_text.set("Make your choice!")
    score_text.set(f"Your Score: {user_score}, Computer's Score: {computer_score}")

    stone_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissors_button.config(state=NORMAL)

def play_round(user_choice):
    global user_score, computer_score, current_round

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
        result_text.set("You won this round!")
    elif result == "computer":
        computer_score += 1
        result_text.set("Computer won this round!")
    else:
        result_text.set("This round is a draw!")

    current_round += 1
    round_text.set(f"Round: {current_round}/{total_rounds}")

    if current_round >= total_rounds:
        if user_score > computer_score:
            messagebox.showinfo("Game Over", f"You are the overall winner! \nFinal Score - You: {user_score}, Computer: {computer_score}")
        elif user_score < computer_score:
            messagebox.showinfo("Game Over", f"The computer wins overall. \nFinal Score - You: {user_score}, Computer: {computer_score}")
        else:
            messagebox.showinfo("Game Over", f"It's a tie overall! \nFinal Score - You: {user_score}, Computer: {computer_score}")
        root.quit()
    else:
        score_text.set(f"Your Score: {user_score}, Computer's Score: {computer_score}")

# Main GUI application
root = ttk.Window(themename="darkly")
root.geometry('500x300')
root.title("Stone, Paper, Scissors")

# GUI Widgets
ttk.Label(root, text="Enter the number of rounds:", font=("Helvetica", 16)).pack(pady=10)
round_entry = ttk.Entry(root, font=("Helvetica", 16))
round_entry.pack()

start_button = ttk.Button(root, text="Start Game", command=start_game, bootstyle=SUCCESS)
start_button.pack(pady=10)

round_text = ttk.StringVar()
round_text.set("Round: 0/0")
ttk.Label(root, textvariable=round_text, font=("Helvetica", 14)).pack()

result_text = ttk.StringVar()
result_text.set("Make your choice!")
ttk.Label(root, textvariable=result_text, font=("Helvetica", 14)).pack()

score_text = ttk.StringVar()
score_text.set("Your Score: 0, Computer's Score: 0")
ttk.Label(root, textvariable=score_text, font=("Helvetica", 14)).pack()

frame = ttk.Frame(root)
frame.pack(pady=20)

stone_button = ttk.Button(frame, text="Stone", command=lambda: play_round("stone"), state=DISABLED, bootstyle=SUCCESS)
stone_button.grid(row=0, column=0, padx=10)

paper_button = ttk.Button(frame, text="Paper", command=lambda: play_round("paper"), state=DISABLED, bootstyle=SUCCESS)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = ttk.Button(frame, text="Scissors", command=lambda: play_round("scissors"), state=DISABLED, bootstyle=SUCCESS)
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()
