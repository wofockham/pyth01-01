# In it, prompt the user for their name. Then, prompt them for their favorite food.
name = input("Please enter your name: ")
food = input("Please enter your favourite food: ")

output = "Your name is {0} and your favourite food is {1}.".format(name, food)

# Using write, create a file called about_me.txt.
about_me = open('about_me.txt', 'w')

# In about_me.txt, write out the name and favorite food in a sentence.
about_me.write(output)
about_me.close()
