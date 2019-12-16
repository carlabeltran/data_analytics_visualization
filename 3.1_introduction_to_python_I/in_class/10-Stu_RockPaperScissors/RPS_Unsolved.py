# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
print(f"You picked {user_choice}.")
print(f"Computer picked {computer_choice}")

if user_choice == "r" and computer_choice == "p":
  print(f"You lost!")
if user_choice == "r" and computer_choice == "s":
  print(f"You won!")
if user_choice == "r" and computer_choice == "r":
  print(f"You tied!")
if user_choice == "p" and computer_choice == "p":
  print(f"You tied!")
if user_choice == "p" and computer_choice == "s":
  print(f"You lost!")
if user_choice == "p" and computer_choice == "r":
  print(f"You won!")
if user_choice == "s" and computer_choice == "p":
  print(f"You won!")
if user_choice == "s" and computer_choice == "s":
  print(f"You tied!")
if user_choice == "s" and computer_choice == "r":
  print(f"You lost!")
if user_choice not in options:
  print(f"{user_choice} is not a valid option")
  print(f"Next time, choose one of the following options: 'r', 'p', or 's'")

