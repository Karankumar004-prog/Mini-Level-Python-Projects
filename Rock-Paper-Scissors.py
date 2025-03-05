import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

choice_1 = int(input("What choice will you make? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if choice_1 < 0 or choice_1 >= 3:
    print("Invalid input, You lose!!! Loser!!!")
else:
    print("So your choice is:\n", game[choice_1])

    computer_choice = random.randint(0, 2)
    print("Computer choice is:\n", game[computer_choice])

    if choice_1 == computer_choice:
        print("It's a Draw. Lets try again...")
    elif choice_1 ==0 and computer_choice == 1:
        print("You Lose. Better Luck Next time.")
    elif choice_1 == 1 and computer_choice ==2:
        print("You Lose. Better Luck Next time.")
    elif choice_1 == 2 and computer_choice == 0:
        print("You Lose. Better Luck Next time.")
    elif choice_1 ==1 and computer_choice == 0:
        print("You Won. Where is the party?")
    elif choice_1 == 2 and computer_choice ==1:
        print("You Won. Where is the party?")
    elif choice_1 == 0 and computer_choice == 2:
        print("You Won. Where is the party?")
    else:
        print("Invalid input, You lose!!! Loser!!!")
