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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice < 3:
    print("Your Choice")
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer Choice")
print(game_images[computer_choice])

if user_choice > 3 and user_choice < 0:
    print("Invalid Input")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif computer_choice == 0 and user_choice == 2:
    print("You Loose!")
elif computer_choice > user_choice:
    print("You Loose!")
elif user_choice > computer_choice:
    print("You Win!")
elif user_choice == computer_choice:
    print("Its a Draw!!!")


