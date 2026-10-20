# #Single Inheritance Example

# class parent:
#     def __init__ (self, name):
#         self.name = name

#     def greet (self):
#         print(f"{self.name} Says Hello")

# class child(parent): # Child class inheriting from parent class
#     def play(self):
#         print(f"{self.name} is playing.")


# child = child("Babu") # Create an instance of the child class

# child.greet() # Babu Says Hello
# child.play() # Babu is playing.

#----------------------------------------------------------

# #Multilevel Inheritance Example

# class grandparent: # Grandparent class
#     def __init__(self, name):
#         self.name = name
#     def story(self):
#         print(f"{self.name} tells a story.")
# class parent(grandparent): # Parent class inheriting from grandparent class
#     def work(self):
#         print(f"{self.name} is working.")
# class child(parent): # Child class inheriting from parent class
#     def play(self):
#         print(f"{self.name} is playing.")   

# Child = child("Babu") # Create an instance of the child class
# Child.story() # Babu tells a story.
# Child.work() # Babu is working.
# Child.play() # Babu is playing.

#----------------------------------------------------------

# #Hierarchical Inheritance Example
# class parent:
#     def __init__ (self, name):
#         self.name = name

#     def greet (self):
#         print(f"{self.name} Says Hello")

# class child1(parent): # Child class inheriting from parent class
#     def play(self):
#         print(f"{self.name} is playing.")

# class child2(parent): # Child class inheriting from parent class
#     def play(self):
#         print(f"{self.name} is studying.")

# Child1 = child1("Babu") # Create an instance of the child class

# Child1.greet() # Babu Says Hello
# Child1.play() # Babu is playing.

# Child2 = child2("Bobby") # Create an instance of the child class
# Child2.greet() # Bobby Says Hello
# Child2.play() # Bobby is studying.

#----------------------------------------------------------

# #Multiple Inheritance Example

# class father:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"{self.name} says hello to Father.")

# class mother(father):
    
#     def greet(self):
#         print(f"{self.name} says hello to Mother.")
#         super().greet() # Call the greet method of the father class
        

# class child(mother, father): # Child class inheriting from both father and mother classes. Follows the method resolution order (MRO) which is mother -> father -> child
    
#     def greet(self):
#         print(f"{self.name} says hello.")
#         super().greet() # Call the greet method of the mother class, which will call the greet method of the father class

# Child1 = child("Babu") # Create an instance of the child class
# Child1.greet() # Babu says hello to Mother. Babu says hello to Father.

#----------------------------------------------------------
##Hybrid Inheritance Example

# class grandfather:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"{self.name} says hello to Grandfather.")

# class father(grandfather):
#     def greet(self):
#         print(f"{self.name} says hello to Father.")
#         super().greet() # Call the greet method of the grandfather class

# class mother(grandfather):
#     def greet(self):
#         print(f"{self.name} says hello to Mother.")
#         super().greet() # Call the greet method of the grandfather class

# class child(mother, father): # Child class inheriting from both father and mother classes. Follows the method resolution order (MRO) which is mother -> father -> child

#     def greet(self):
#         print(f"{self.name} says hello.")
#         super().greet() # Call the greet method of the mother class, which will call the greet method of the father class

# Child1 = child("Babu") # Create an instance of the child class
# Child1.greet() # Babu says hello to Mother. Babu says hello to Father.
