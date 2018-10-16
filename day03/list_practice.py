# Save a list with the numbers 2, 4, 6, and 8 into a variable called numbers.
numbers = [2, 4, 6, 8]

# Print the max of numbers.
# max_number = max(numbers)
# print("The maximum number is", max_number)
print("The maximum number is", max(numbers))

# Pop the last element in numbers off; re-insert it at index 2.
moving_number = numbers.pop()
numbers.insert(2, moving_number)

# Pop the second number in numbers off.
numbers.pop(1)

# Append 3 to numbers.
numbers.append(3)

# Print out the average number (divide the sum of numbers by the length).
average = sum(numbers) / len(numbers) # Ask Dr Google if you can't remember averages.
print("The average is", average)

# Print numbers.
print(numbers)
