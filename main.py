
#<----Object Oriented Programming---->

# mylist = [12,3,4,5]
# mylist.append(4)
# print(mylist)

class Dog():
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name





myDog = Dog(breed="Chow", name="Spike")
herDod = Dog(breed="Lab", name="Bear")
print(myDog.breed)
print(herDod.name)