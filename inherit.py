#simple inheritance example

class Animal:
    def __init__(self, name): # Constructor for Animal class
        self.name = name # Instance variable for the name of the animal
    def speak(self): # Method for the Animal class that prints a generic sound
        print(f"{self.name} makes a sound.") # Prints the sound the animal makes
    
class Dog(Animal): # Dog class inherits from Animal class
    def __init__ (self, name): # Constructor for Dog class, it overrides the constructor of the Animal class, Constructor Overloading
        super().__init__(name) # Call the constructor of the parent class (Animal)
        self.behavior = "Friendly" # Instance variable for the behavior of the dog
    #def speak(self): # Method for the Dog class that overrides the speak method of the Animal class Method Overriding
    def speak1(self): # it can inherit methods from the parent class, but if you want to change the behavior of a method, you can override it in the child class.
         print(f"{self.name} barks. And he's {self.behavior}") # Prints the sound the dog makes

animal = Animal("Sheep") # Create an instance of the Animal class
animal.speak() # Output: Sheep makes a sound.

dog = Dog("BOY") # Create an instance of the Dog class
#dog.speak() # Output: BOY makes a sound. From the parent class Animal
#dog.speak1() # Output: BOY barks. From the child class Dog
#behavior = input("Enter the behavior of the dog: ") # Get user input for the behavior of the dog
dog.speak1()

# #Super Keyword Example

# class Animal:
#     def __init__(self): # Constructor for Animal class
#         self.name = "Buddy" # Instance variable for the name of the animal
#     def speak(self): # Method for the Animal class that prints a generic sound
#         print(f"{self.name} makes a sound.") # Prints the sound the animal makes
    
# class Dog(Animal): # Dog class inherits from Animal class
#     def __init__ (self, breed): # Constructor for Dog class, it overrides the constructor of the Animal class, Constructor Overloading
#         super().__init__() # Call the constructor of the parent class (Animal)
#         self.breed = breed # Instance variable for the behavior of the dog
#     #def speak(self): # Method for the Dog class that overrides the speak method of the Animal class Method Overriding
#     def speak(self): # it can inherit methods from the parent class, but if you want to change the behavior of a method, you can override it in the child class.
#          super().speak() # Call the speak method of the parent class (Animal)
#          print(f"{self.name} barks. And he's {self.breed}") # Prints the sound the dog makes
    

# dog = Dog("German Shepherd") # Create an instance of the Dog class

# dog.speak()

