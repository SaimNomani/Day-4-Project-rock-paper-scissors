import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
options = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input("chose from 0 for 'rock', 1 for 'paper' or 2 for 'scissors': \n"))
if user_choice >= 3 or user_choice < 0:
    print("invalid number")
else:
    print(f"your choice\n{options[user_choice]}")
    print(f"computer choice:\n{options[computer_choice]}")
    if computer_choice == user_choice:
        print("it's a draw\n")
    elif user_choice == 0 and computer_choice == 2:
        print("you win")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif computer_choice < user_choice:
        print("you win")


