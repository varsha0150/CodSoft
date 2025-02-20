import tkinter as tk
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    
    if result == "You Win!":
        user_score += 1
    elif result == "Computer Wins!":
        computer_score += 1
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make Your Choice!")
    score_label.config(text="Score: You 0 - 0 Computer")

# Tkinter Window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make Your Choice!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons for choices
frame = tk.Frame(root)
frame.pack()

for choice in choices:
    btn = tk.Button(frame, text=choice, font=("Arial", 12),bg= "yellow", width=10, command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), bg = "lightgreen",command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()