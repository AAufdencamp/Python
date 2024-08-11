#Class inheritance: a class can inherit attributes and/or methods of a given superclass
#We can also modify inherited methods from a superclass and tweak them to do extra inside the inheritor class
#Iheritance allows us to build onto existing classes

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")



class Fish(Animal): #to inherit from Animal superclass
    def __init__(self):  #initializer to define attributes and methods of Fish class
        super().__init__()  #initialize everything that the superclass Animal has into our fish class

    def breathe(self):  #here we modify the inherited Animal breathe() method
        super().breathe() #by calling on the superclass and calling breathe() on it
        print("doing this underwater.") #this Fish breathe() method can do everything it inherited from the
                                        # Animal breath() method but extra

    def swim(self):
        print("moving in water")

nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog): #We create a class Labrador (the sublcass) that inherits from Dog class (the superclass)
    def __init__(self):   #The call to super() in the initialiser is recommended, but not strictly required.
        self.temperament = "friendly"
        self.is_a_good_boy = True

    def bark(self):
        super().bark() #we extend the functionality of the bark() method
        print("Greetings, good sir. How do you do?")


#cooper = Labrador()
#cooper.bark()

doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")
sparky.bark() #we extend the functionaly of the bark() method

#slicing from lists and tuples
#list[a:b] we extract a set of items from a list from postion a to position b but EXCLUDING b
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])

#extract from a list from starting index all the way to the end or last index
print(piano_keys[2:])

#extract all indices from the start through but excluding a given index
print(piano_keys[:4])

#adding a third argument into slicing bracket notation gives the desired step
print(piano_keys[:5:2])

print(piano_keys[::2]) #extract every other index

print(piano_keys[::-1]) #starting with last indices extract index at each decreasing -1 step

#recall that tuples are defined by a set of parentheses with items inside separated by commas.

piano_tuple = ("do", "re", "me", "fa", "so", "la", "ti")

print(piano_tuple[2:5])