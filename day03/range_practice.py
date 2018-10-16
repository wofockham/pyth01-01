# Create a list of colors.
colors = ['red', 'blue', 'green', 'aliceblue', 'ultraviolet']

# Using a for loop, print out the list.
for color in colors:
    print(color)

# Using range, set each item in the list to be the number of characters in the list.
for index in range(len(colors)):
    colors[index] = len(colors[index])
    # print(index, colors[index], len(colors[index]))

# Print the list.
print(colors)
