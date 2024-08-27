import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector as mysql
import bcrypt

def connect():
    try:
        conn = mysql.connect(
            user = "root",
            password = "Test@123",
            database = "rps",
            host = "localhost",
            port = 3306
        )
        return conn
    except Exception as err:
        print(err)
        raise

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
    connect()
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

    stone_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    start_button.config(state=tk.DISABLED)

def save_score(user_score, computer_score, win_status):
    connection = connect()
    cursor = connection.cursor()
    try:
        query = """
        insert into user_scores (username, score, cpu_score, win_loss_status) values ('p1', %s, %s, %s)
        """
        cursor.execute(query, (user_score, computer_score, win_status))
        connection.commit()
        connection.close()
    except Exception as err:
        print(err)
        connection.close()
    
def play_round(user_choice):
    global user_score, computer_score, current_round

    computer_choice = get_computer_choice()
    computer_text.set(f"Computer's Choice: {computer_choice}")
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

    win_status = 'draw'
    
    if current_round >= total_rounds:
        if user_score > computer_score:
            messagebox.showinfo("Game Over", f"You are the overall winner! \nFinal Score - You: {user_score}, Computer: {computer_score}")
            win_status = 'win'
        elif user_score < computer_score:
            messagebox.showinfo("Game Over", f"The computer wins overall. \nFinal Score - You: {user_score}, Computer: {computer_score}")
            win_status = 'loss'
        else:
            messagebox.showinfo("Game Over", f"It's a tie overall! \nFinal Score - You: {user_score}, Computer: {computer_score}")
        save_score(user_score, computer_score, win_status)
        root.quit()
    else:
        score_text.set(f"Your Score: {user_score}, Computer's Score: {computer_score}")

def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    connection = connect()
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
        connection.commit()
        play_game()
        print("User registered successfully")
    except mysql.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def authenticate_user(username, password):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        print("Login successful")
        cursor.close()
        connection.close()
        return True
    else:
        print("Invalid username or password")
        cursor.close()
        connection.close()
        return False

def main_menu():
    global username, password
    choice = input("1. Register\n2. Login\nChoose an option: ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if authenticate_user(username, password):
            play_game()
        else:
            print("Authentication failed")
    else:
        print("Invalid choice")

def play_game():
    global root
    root = tk.Tk()
    root.title("Stone, Paper, Scissors")

    tk.Label(root, text="Enter the number of rounds:").pack(pady=10)
    global round_entry
    round_entry = tk.Entry(root)
    round_entry.pack()

    global start_button
    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.pack(pady=10)

    global round_text
    round_text = tk.StringVar()
    round_text.set("Round: 0/0")
    tk.Label(root, textvariable=round_text).pack()

    global result_text
    result_text = tk.StringVar()
    result_text.set("Make your choice!")
    tk.Label(root, textvariable=result_text).pack()

    global computer_text
    computer_text = tk.StringVar()
    computer_text.set("Computer's choice: ")
    tk.Label(root, textvariable=computer_text).pack()

    global score_text
    score_text = tk.StringVar()
    score_text.set("Your Score: 0, Computer's Score: 0")
    tk.Label(root, textvariable=score_text).pack()

    global frame
    frame = tk.Frame(root)
    frame.pack()

    global stone_button
    stone_button = tk.Button(frame, text="Stone", command=lambda: play_round("stone"), state=tk.DISABLED)
    stone_button.grid(row=0, column=0)

    global paper_button
    paper_button = tk.Button(frame, text="Paper", command=lambda: play_round("paper"), state=tk.DISABLED)
    paper_button.grid(row=0, column=1)

    global scissors_button
    scissors_button = tk.Button(frame, text="Scissors", command=lambda: play_round("scissors"), state=tk.DISABLED)
    scissors_button.grid(row=0, column=2)

    root.mainloop()
    pass

if __name__ == "__main__":
    main_menu()

