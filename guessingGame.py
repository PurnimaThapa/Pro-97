import random

number = random.randrange(1, 9)

chances=0

print("Print a number between 1 and 9")
print("you have 5 chances")

while chances < 5:
    guess = int(input("Guess a number between 1 and 9: "))
    chances = chances + 1

    if guess < number:
        print("Too low! Guess a number higher than ", guess)
        
    if guess > number:
        print("Too high! Guess a number lower than ", guess)

    if guess == number:
        print("You win!!!")
        break

    if not chances < 5:
        print("You lose! The number was", number) 
        