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

# user =int(input("Enter the number 0 for Rock, 1 for Paper and 2 for Scissors: "))
# if user==0:
#     print(rock)
# elif user==1:
#     print(paper)
# elif user==2:
#     print(scissors)
# elif user>=3:
#     print("Please enter numbers between 0 to 2.")
#
# random_computer = random.randint(0,2)
# print("Computer chose: ")
# print(random_computer)
# if random_computer==0:
#     print(rock)
# elif random_computer==1:
#     print(paper)
# else:
#     print(scissors)
#
# if random_computer==0 and user==1:
#     print("You won!")
# elif random_computer==1 and user==2:
#     print("You won!")
# elif random_computer==2 and user==0:
#     print("You won!")
# elif user==0 and random_computer==1:
#     print("You lose!")
# elif user==1 and random_computer==2:
#     print("You lose!")
# elif user==2 and random_computer==0:
#     print("You lose!")
# elif random_computer==user:
#     print("draw")

game_image = [rock,paper,scissors]
user_choice = int(input("What would you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))
print(game_image[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice} ")
print(game_image[computer_choice])

if user_choice>=3 or user_choice<0:
    print("Invalid value entered. Enter between 0 to 2.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice == user_choice:
    print("Draw!")
