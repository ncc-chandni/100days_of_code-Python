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
images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("You chose")
if user >= 3 or user <= -1:
    print("Invalid number. You lose!")
else:
    print(images[user])

    computer = random.randint(0,2)
    print("Computer chose:")
    print(images[computer])

    if user == 0 and computer == 2 or user == 1 and computer == 0:
        print("You win!")
    elif user == 0 and computer == 1 or user == 1 and computer == 2:
        print("You lose")
    elif user == computer:
        print("Its a draw")
        