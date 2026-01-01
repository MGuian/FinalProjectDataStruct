#Guian Jaundell R. Manalo
#CPE3B
##Lesson 13 Exercise 2

class User:         #Class to represent User Profiles
    def __init__(self, first_name, last_name, age, sex, email, address):        #Initialize user attributes
        self.first_name = first_name        #Assigning Attributes
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.email = email
        self.address = address
        self.login_attempts = 0     #Attribute to control the number of login attempts
    def describe_user(self):            #Method to print the user's information
        print('\nUser Profile: ')           #Print all the user's information
        print('Name: ' + self.first_name + ' ' + self.last_name)
        print('Age: ' + str(self.age))      #use str to convert integer to string
        print('Sex: ' + self.sex)
        print('Email: ' + self.email)
        print('Address: ' + self.address)
    def greet_user(self):           #Method to print a personalized greeting to the user
        print('\nHello, ' + self.first_name + ' ' + self.last_name + '! Welcome back to the platform.\n\n')
    def increment_login_attempts(self):         #Method to increment the login attempts by 1
        self.login_attempts += 1
    def reset_login_attempts(self):         #Methods to reset the login attempts
        self.login_attempts = 0
    def message_login_attempts(self):       #Methods to show user's the login attempts
        print(self.first_name + ' ' + self.last_name + "'s Login Attempts: " + str(self.login_attempts))        #use str to convert integer to string
try:
    #Users Instances
    user1 = User("Guian Jaundell", "Manalo", 20, "Male", "2321171@ub.edu.ph", "Mabini, Lipa, Batangas, Philippines")
    user2 = User("Jaundell", "Manalo", 19, "Male", "232117@ub.edu.ph", "Lipa, Batangas, Philippines")
    user3 = User("Guian", "Manalo", 21, "Male", "232171@ub.edu.ph", "Philippines")
    #Call the describe_user and greet_user methods for each user
    user1.describe_user()
    user1.greet_user()
    user2.describe_user()
    user2.greet_user()
    user3.describe_user()
    user3.greet_user()
    #Call the increment_login_attempts several times
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.message_login_attempts()  #Show user total Login Attempts
    #Call the reset_login_attempts to reset the login attempts
    user1.reset_login_attempts()
    user1.message_login_attempts()  #Show user total Login Attempts after reset
except Exception as e:          #Handles Error
    print('\nError Found...')
