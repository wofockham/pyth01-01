# Open for read mode your existing hello.txt.
hello_file = open('hello.txt')

# Read() the file and save the contents into a variable, file_contents.
file_contents = hello_file.read()

# Under that, using write, create a file called my_file_output.txt.
output_file = open('my_file_output.txt', 'w')

# In my_file_output.txt, write what you read from a_file.txt.
output_file.write(file_contents)

hello_file.close()
output_file.close()
