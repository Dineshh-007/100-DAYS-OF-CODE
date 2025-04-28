from art import logo
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

choice=input("Do you want to play a game of Blackjack?"
             "Type 'y' or 'n': ")

is_game_over=False

while not is_game_over:
    if choice=='y':
        print(logo)
        user_card=[]
    
        computer_card=[]
    
        while len(user_card) < 2:
            user_card.append(random.choice(cards))
    
        user_score = sum(user_card)
        print(f"Your cards: {user_card},Current Score : {user_score}")
    
        while len(computer_card)<2:
            computer_card.append(random.choice(cards))
    
        computer_score=sum(computer_card)
        print(f"Computer's first cards: {computer_card[0]}")
        
        if user_score == 21:
            print("You won")
            is_game_over=True
        elif computer_score == 21:
            print("Computer won")
            is_game_over=True

        if user_score==0 or computer_score==0 or user_score>21:
            if 11 in user_card:
                user_card.remove(11)
                user_card.append(1)


            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal=='y':
                user_card.append(random.choice(cards))
                user_score=sum(user_card)
                print(f"Your cards: {user_card}, current score: {user_score}")
                print(f"Computer's first cards: {computer_card[0]}")
                if user_score > 21:
                    is_game_over=True
                else:
                    print("Type 'y' to get another card, type 'n' to pass")