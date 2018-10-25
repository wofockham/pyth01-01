foods_list = ["hotdogs", "poutine", "butterscotch"]
foods_set = {"hotdogs", "poutine", "butterscotch"}
foods_tuple = ("hotdogs", "poutine", "butterscotch")

also_foods_set = set(foods_list)

# YOUR CODE HERE:

# Add "pizza" anywhere; append "eggs" to the end.
foods_list.insert(2, "pizza")
foods_list.append('eggs')
foods_set.add('pizza')
foods_set.add('eggs')

# Remove "pizza".
foods_list.remove('pizza')
foods_set.remove('pizza')

# Re-assign the element at index 1 to be "popcorn".
foods_list[1] = "popcorn"

# Remove the element at index 2 and re-insert it at index 0.
moving_food = foods_list.pop(2)
foods_list.insert(0, moving_food)

# Print the element at index 0.
print(foods_list[0])
print(foods_tuple[0])

print("******* List:")
for food in foods_list:
    print(food)

print("******* Set:")
for food in foods_set:
    print(food)

print("******* Tuple:")
for food in foods_tuple:
    print(food)
