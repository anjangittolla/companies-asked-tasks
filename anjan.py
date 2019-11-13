import random
n=random.randint(1,50)
chances=5
while chances>0:
    guess = int(input("Guess a number:   "))
    if n>guess:
        chances=chances-1
        print("Your guessing number is less than the actual number",chances)
    elif n<guess:
        chances=chances-1
        print("Your guessing number is more than the actual number",chances)
    else:
        break
print("Your guessing is correct")