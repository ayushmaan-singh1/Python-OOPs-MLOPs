#initiate a class
class employee:
    #special method/magic method/dunder method also called constructor
    def __init__(self) :
        #print("Initiating attributes automatically")
        self.id = 123
        self.salary = 66667
        self.designation = "DevOps Engineer"
        #print("Initiated attributes automatically")
    #Function inside a class is called method
    def travel(self, destination):
        #print("Initiating method/function manually")
        print(f"Employee is now travelling to {destination}")

#creating an object/instance of class
sam = employee()
#print(sam.id) #--> attributes are called itself when you initate, to test uncomment print insie attributes and comment calling of id designation outside sam.id etc it'll be printed automatically
#print(sam.salary)
#print(sam.designation)
#sam.travel("Hyerabad") #--> methods are called manually, to test uncomment print inside method/function and then run it'll not print anything

#Need of constructor is required for it to automatically run required services, for example conneting to db, internet, execute something etc.

print(type(sam))

#any Datatypes  python is class 
#That's why python is called OOPs because every data structure, data type etc are objects made using a class