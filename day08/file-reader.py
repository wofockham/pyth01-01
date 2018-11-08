# my_file = open('hello.txt')
# print( my_file.read() )
# my_file.close()

# Open with 'w' will also create a file if it doesn't exist
my_file = open('hello.txt', 'w') # 'w' is the mode meaning (over)"write"
my_file.write("Apple juice is delcious\n" + "Also whiskey")
my_file.close
