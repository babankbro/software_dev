from dogv2 import *
from catv2 import *


# Create a Dog instance
my_dog = Dog("Buddy", "Golden Retriever", 3)
print(my_dog.bark())
print(my_dog.display_info())

# Create a Cat instance
my_cat = Cat("Whiskers", "Siamese", 2)
print(my_cat.meow())
print(my_cat.display_info())