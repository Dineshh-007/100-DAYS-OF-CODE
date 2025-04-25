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
print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
a=int(input())
choose=[rock,paper,scissors]

computer=random.choice(choose)
if a==0:
    print(rock)
elif a==1:
    print(paper)
elif a==2:
    print(scissors)
else:
    print("Enter a valid one")
    exit()

print("Computer chose:")
print(computer)

if a==0 and computer==rock:
    print("Match draw")
elif a==0 and computer==paper:
    print("Computer won")
elif a==0 and computer==scissors:
    print("You won...")
elif a==1 and computer==rock:
    print("You won...")
elif a==1 and computer==paper:
    print("Match draw")
elif a==1 and computer==scissors:
    print("Computer won")
elif a==2 and computer==rock:
    print("Computer won")
elif a==2 and computer==paper:
    print("You won...")
elif a==2 and computer==scissors:
    print("Match draw")