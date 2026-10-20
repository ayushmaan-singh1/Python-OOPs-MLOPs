#initiate a class
class employee:
    #special method/magic method/dunder method also called constructor
    def __init__(self) : # --> self is a reference to the current instance/Obj of the class in this case sam or any future obj which we don't know will exist, and is used to access variables that belong to the class. #__init__ is a constructor method that is automatically called when an object of the class is created. It is used to initialize the attributes of the class.
        #print("Initiating attributes automatically")
        print(id(self))
        #self.id = 123
        #self.salary = 66667
        #self.designation = "DevOps Engineer"
        #print("Initiated attributes automatically")
    #Function inside a class is called method
    def travel(self, destination):
        #print("Initiating method/function manually")
        print(f"Employee is now travelling to {destination}")

#creating an object/instance of class
sam = employee()
print(id(sam)) #prints the memory address of the object sam, which is the same as the id printed inside the __init__ method, confirming that self refers to the instance sam.
samy = employee()
print(id(samy)) #prints the memory address of the object samy, which is the same as the id printed inside the __init__ method, confirming that self refers to the instance samy.
#print(sam.id) #--> attributes are called itself when you initate, to test uncomment print insie attributes and comment calling of id designation outside sam.id etc it'll be printed automatically
#print(sam.salary)
#print(sam.designation)
#sam.travel("Hyerabad") #--> methods are called manually, to test uncomment print inside method/function and then run it'll not print anything

#Need of constructor is required for it to automatically run required services, for example conneting to db, internet, execute something etc.

print(type(sam))

#any Datatypes  python is class 
#That's why python is called OOPs because every data structure, data type etc are objects made using a class