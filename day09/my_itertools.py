import itertools

# Create a list of colors.
colors = ['aubergine', 'beige', 'green']

# Create a dictionary of hobbies.
hobbies = {
    "tiddlywinks": "yes please",
    "chess": True,
    "lepidoptery": True,
    "golf": False
}

# Chain them together.
chained_list = itertools.chain(colors, hobbies)
chained_list = list(chained_list)

# Print out the chain!
print(chained_list)
