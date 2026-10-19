

import email


class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("Successfully Signedup!!\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first\nBringing SignUp Menu\n")
            self.signup()
            return
        user_name = input("Enter your email: ")
        user_pwd = input("Enter your password: ")
        if user_name == self.username and user_pwd == self.password:
            print(f"You've logged in successfully Welcome: {user_name} \n")
            self.loggedin = True
            self.menu()
            return
            
        elif user_name != self.username or user_pwd != self.password:
            print(f"You've entered wrong username or password try again\n")
            cont = input("Do you want to try again? y/n: ")
            if cont == 'Y' or cont =='y':
                self.signin()
            else:
                self.menu()
        else:
            print("User don't exist signup, exiting now!!\n")
            exit()
    
    
    def post(self):
        if self.loggedin == True:
            txt = input("Enter what you want to post: ")
            print(f"!!Following content has been posted!!\n{txt}")
            self.menu()
        else:
            print("Please Signup or signin first to post\n")
        self.menu()    

    def msg(self):
        if self.loggedin == True:
            msg = input("Enter message for your friend: ")
            frnd = input("Which friend to send the msg: ")
            print(f"!!Following message has been sent To {frnd}!!\n{msg}\n")
            self.menu()
        else:
            print("Please Signup or signin first to msg\n")
        self.menu() 


    def menu(self):
        user_input = input("""Welcome to chatbook!! \n How would you like to Proceed?
                           1.) Press 1 to Signup.
                           2.) Press 2 to Signin.
                           3.) Press 3 to write a post
                           4.) Press 4 to msg a friend
                           5.) Press anything else to exit
                           Provide your input: """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            #print("You've posted")
            self.post()
        elif user_input == '4':
            self.msg()
            #print("You've msged")
        else :
            print("You've exited")
            exit()

     


obj = chatbook()