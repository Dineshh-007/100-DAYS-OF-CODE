print("Welcome to the tip calculator!")
print(" ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
amount= (bill+(bill*tip/100))/5

print(f"Each person should pay: {round(amount,2)}")