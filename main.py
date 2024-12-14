import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = ''
    
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win!'
    else:
        result = 'You lose!'
    
    messagebox.showinfo('Result', f'You chose {user_choice}, computer chose {computer_choice}. {result}')

# Setting up the main window
root = tk.Tk()
root.title('Rock, Paper, Scissors')

# Adding buttons for Rock, Paper, Scissors
tk.Button(root, text='Rock', command=lambda: play('rock')).pack(side=tk.LEFT, padx=20)
tk.Button(root, text='Paper', command=lambda: play('paper')).pack(side=tk.LEFT, padx=20)
tk.Button(root, text='Scissors', command=lambda: play('scissors')).pack(side=tk.LEFT, padx=20)

# Start the GUI event loop
root.mainloop()
