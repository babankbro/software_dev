from dogv2 import *
from catv2 import *


# Creating 2 Cat instances
cat1 = Cat("Whiskers", "Siamese", 2)
cat2 = Cat("Shadow", "Maine Coon", 3)
# Creating 3 Dog instances
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Beagle", 4)
dog3 = Dog("Lucy", "Border Collie", 1)

# Adding all instances to the same list
pets = [cat1, cat2, dog1, dog2, dog3]
# Iterating over the list and calling makeSound() on each pet
for i in range(len(pets)):
    pet = pets[i]
    print(pet.make_sound())