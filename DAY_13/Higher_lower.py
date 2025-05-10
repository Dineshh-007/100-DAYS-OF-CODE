import random

from art import logo, vs
from game_data import data

print(logo)

is_continue=False
def compare(dict1,dict2):
    if dict1['follower_count'] < dict2['follower_count']:
        return 'B'
    else:
        return 'A'

A=random.choice(data)
count=0

while not is_continue:
    B=random.choice(data)
    while A == B:
        B = random.choice(data)
    print(f"Compare A:{A['name']}, a {A['description']}, from {A['country']}")

    print(vs)

    print(f"Against B:{B['name']}, a {B['description']}, from {B['country']}")

    user=input("Who has more followers? Type 'A' or 'B': ").lower()

    correct_choice=compare(A,B).lower()

    if correct_choice == user:
        print("You won")

    else:
        print(f"You lose!! Your final score: {count}")
        is_continue = True
        break

    A=B
    count+=1
    print(f"You're right...! Current score: {count}")