import random
guess = int(input("Guess a number between 1 and 9 (including 1 and 9) : "))
number = random.randrange(1,10)
print("The number is ",number)
if guess == number:
    print("Your guess is exactly right")
elif guess < number:
    print("Your guess is too low ")
else:
    print("Your guess is too high")
