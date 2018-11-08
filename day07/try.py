my_num = None

while my_num is None:
  try:
      my_num = int(input("Please give me a number:"))
  except ValueError:
      print("That was not good input, please try again!")

print("Thanks for typing the number", my_num)
