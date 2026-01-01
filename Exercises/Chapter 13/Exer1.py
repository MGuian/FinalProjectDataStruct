#Guian Jaundell R. Manalo
#CPE3B
##Lesson 13 Exercise 1

class User:         #Class to represent User Profiles
    def __init__(self, first_name, last_name, age, sex, email, address):        #Initialize user attributes
        self.first_name = first_name        #Assigning Attributes
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.email = email
        self.address = address
    def describe_user(self):            #Method to print the user's information
        print('\nUser Profile: ')           #Print all the user's information
        print('Name: ' + self.first_name + ' ' + self.last_name)
        print('Age: ' + str(self.age))      #use str to convert integer to string
        print('Sex: ' + self.sex)
        print('Email: ' + self.email)
        print('Address: ' + self.address)
    def greet_user(self):           #Method to print a personalized greeting to the user
        print('\nHello, ' + self.first_name + ' ' + self.last_name + '! Welcome back to the platform.\n\n')
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
except Exception as e:          #Handles Error
    print('\nError Found...')