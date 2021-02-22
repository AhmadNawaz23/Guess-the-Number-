# Guess the Number Game
import random

print("Welcome, What is your name ?")
name = input()

print("Hello, "+ name + "I am thinking of a number between 1 to 10")
secret_num = random.randint(1,10)

for guesses in range(0,4):
    print("Take a guess ")
    guess = int(input())

    if guess < secret_num:
        print("Your guess is low.")
    elif guess > secret_num:
        print("Your guess is high.")
    else:
        break #this condition is for the correct guess!
if guess == secret_num:
    print("Good job," + name + "your guessed my number in" + str(guesses) + "guess" )

else:
    print("Nope the Number i was thinking of was " + str(secret_num))
