# set up the correct answer TODO: make this a random number
answer = "5"
guess = input("What number am I thinking of: ")

while guess != answer:
    guess = input("Wrong! Guess again: ")

print("Yes, you got it")
