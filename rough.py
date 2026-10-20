#list = [1, 2, '3'] #--> it's class
#str = "hello" #--> it's class
#int = 1269 #--> it's class

#list.clear() #--> clear method
#str = str.capitalize() #--> capitalize method
#print(list, str, int)
#print(type(list), type(str), type(int))

#any Datatypes  python is class 
#That's why python is called OOPs because every data structure, data type etc are objects made using a class

# from oops_proj import chatbook

# user1 = chatbook()
# user1.signin() #--> calling a method, a method is a function inside a class

from calendar import c
from oops_proj import chatbook

user1 = chatbook()

print(user1.id) # Calling id attribute of the user1 instance of the chatbook class

# Using static method directly from the class without creating an instance of the class
chatbook.set_id(111) # Setting the static variable __user_id of the chatbook class to 111 using the set_id method of the chatbook class

user2 = chatbook() # Creating another instance of the chatbook class
print(user2.id) # Calling get_id method of the user1 instance of the chatbook class

user3 = chatbook() # Creating another instance of the chatbook class
print(user3.id)
#user2 = chatbook() # Creating another instance of the chatbook class

#print(user2.id) # Calling id attribute of the user2 instance of the chatbook class

#user3 = chatbook() # Creating another instance of the chatbook class

#print(user3.id) # Calling id attribute of the user3 instance of the chatbook class

#print(user1.name) # Accessing public attribute directly, this is allowed because the attribute is public and can be accessed from outside the class.
#print(user1._chatbook__name) # Accessing the private attribute using name mangling, this is required because the attribute is private and cannot be accessed directly from outside the class. The name of the private attribute is changed to _ClassName__attributeName, where ClassName is the name of the class and attributeName is the name of the private attribute. This is done to prevent accidental access to private attributes from outside the class.

#print(user1.get_name()) # Accessing the private attribute using the getter method, this is the recommended way to access private attributes from outside the class. The getter method is a public method that returns the value of the private attribute.
#user1.set_name("Rancho") # Setting the private attribute using the setter method, this is the recommended way to set private attributes from outside the class. The setter method is a public method that sets the value of the private attribute.
#print(user1.get_name()) # Accessing the private attribute using the getter method again to verify that the value has been updated. The getter method returns the updated value of the private attribute.
