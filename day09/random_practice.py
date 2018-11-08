import random

print(random.randint(1, 100))
deck = ["ten", "jack", "queen", "king", "ace"]

random_card = random.choice(deck)
print(random_card)

random.shuffle(deck) # destructive function - loses the original order
print(deck)
