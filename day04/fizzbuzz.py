def fizzbuzz(i):
    # Test the most specific or exceptional cases first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for test_candidate in range(1, 101):
    fizzbuzz(test_candidate)
