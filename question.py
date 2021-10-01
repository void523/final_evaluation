'''
Class “Pet” should include the following methods:


__init__ () : Accepts three arguments: self, species(default None), and name(default “”). Stores species and name as data attributes. Raises Error, if the species is not one of the following : 'dog', 'cat', 'horse', 'hamster'.


__str__() : Returns a string which depends on whether the pet is named or not.

If named: "Species of: xxx, named xyy", where xxx is the species data attribute and yyy is the name data attribute

otherwise: "Species of: xxx, unnamed", where xxx is the species data attribute



Class “Dog” (which is a subclass of class “Pet”) should include the following methods :


__init__() : Accepts three arguments: self, name(default “”), and chases(default“Cats”).

Uses the constructor for class “Pet” to store species(“Dog”) and ‘name’ as data attributes.

Stores ‘chases’ as a data attribute.


__str__() : Returns a string which depends on whether the dog is named or not.

If named: "Species of: Dog, named yyy, chases zzz", where yyy is the name data attribute (as above) and zzz is the chases data attribute.

Otherwise: "Species of: Dog, unnamed,chases zzz", where zzz is the chases data attribute


Class “Cat” (which is a subclass of class “Pet”) should include the following methods:


1. __init__ () : Accepts three arguments: self, name(default “”), and hates(default “Dogs”).

Uses the constructor for class “Pet” to store species(“Cat”) and ‘name’ as data attributes.

Stores ‘hates’ as a data attribute.


2. __str__ () : Returns a string which depends on whether the cat is named or not.

If named: "Species of: Cat, named yyy, hateszzz", where yyy is the name data attribute(as

above) and zzz is the hates data attribute.

Otherwise: "Species of: Cat, unnamed, hateszzz", where zzz is the hates data attribute.


- Write a main() class to create five "dogs" and three "cats"
- Store these objects in a dictionary with Keys as "Dog", "Cat"
- Demonstrate the working of the Dog and Cat objects
'''

class Pet:
    def __init__(self,species = " ",name =None):
        self.species = species
        self.name = name

    def check_species(self):
        if self.species not in ["dog","cat","horse","hamster"]:
            print("Error, unknown species!")

    def __str__(self):
        if self.name == "" :
            return f"Species of {self.species} unnamed"
        else:
            return f"Species of {self.species} named {self.name}"


class Dog(Pet):
    def __init__(self,name= "",chases = "cats"):
        self.name = name
        self.chase = chases

    def chases(self):
        return self.chases()


    def __str__(self):
        if self.name == "" :
            return f"Species of Dog unnamed chases {self.name}"
        else:
            return f"Species of Dog named {self.name} chases {self.chase}"


class Cat(Pet):
    def __init__(self,name = "", hates ="Dogs"):
        self.name = name
        self.hate = hates

    def hates(self):
        return self.hates()

    def __str__(self):
        if self.name == "" :
            return f"Species of Cat unnamed hates {self.hate}"
        else:
            return f"Species of Dog named {self.name} chases {self.hate}"


if __name__ == '__main__':
    pets = {"dogs":[],"cats":[]}
    print("""
    please enter your pet names\n
    Only five dogs and three cats allowed\n
    """)
    print('Taking the Dog names')
    c = 0
    while c!=5:
        dog_ = input("Enter dog name: ")
        pets["dogs"] = dog_
        c+=1
        if c == 5:
            print("Taking the Cat names")
            n = 0
            while n != 3:
                cat_ = input('Enter the cat name: ')
                pets["cats"] = cat_
                n += 1
                if c == 3:
                    break

    for item in range(len(pets)):
        dog_1 = Dog(pets["dogs"][item])
        print(dog_1)
        cat_1 = Cat(pets["cats"][item])
        print(cat_1)

