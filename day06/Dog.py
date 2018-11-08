class Dog():
  total_dogs = 0
  def __init__(self, name="", age=0):
    self.name = name
    self.age = age
    Dog.total_dogs += 1 #  We can increment this here!
    print(name, "created:")

  def bark_hello(self):
    print("Woof! I am called", self.name, "; I am", self.age, "human-years old.")
    print("There are", Dog.total_dogs, "dogs in this room!")

# # Declare the object instances.
# gracie = Dog("Gracie", 8)
# spitz = Dog("Spitz", 5)
# buck = Dog("Buck", 3)
#
# # Test them out!
# gracie.bark_hello()
# print("This dog's name is", gracie.name)
# print("This dog's age is", gracie.age)
# spitz.bark_hello()
# buck.bark_hello()
