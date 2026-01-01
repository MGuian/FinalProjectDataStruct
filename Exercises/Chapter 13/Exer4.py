#Guian Jaundell R. Manalo
#CPE3B
##Lesson 13 Exercise 4

class Restaurant:       #Class to represent the restaurant
    def __init__(self, restaurant_name, cuisine_type):      #Initialize the name of the restaurant and cuisine type
        self.restaurant_name = restaurant_name          #Assigning of attributes
        self.cuisine_type = cuisine_type
        self.number_served = 0       #Attribute to control the number of number of served
    def describe_restaurant(self):          #Method to Print info of the restaurant
        print('\nRestaurant Name: ' + self.restaurant_name)
        print('Type of Cuisine: ' + self.cuisine_type)
        print('Number Served: ' + str(self.number_served))
    def open_restaurant(self):          #Method to Print the message that the restaurant is open
        print('\n' + self.restaurant_name + ' is open today.\n')
    def set_number_served(self, num):    #Method to set the number of customers served
        self.number_served = num     #Update the number_served attribute
    def increment_number_served(self, add):       #Method to increment the number of customers served
        self.number_served += add         #Add the increment value to the current number_served
try:
    #Instance of restaurant
    restaurant = Restaurant("Pizza Hut", "Italian-American")
    #Print the restaurant_name attribute and cuisine_type attribute individually
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    #Call the describe_restaurant to print the restaurant information and open_restaurant to print that restaurant is open
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    print('Number Served: ' + str(restaurant.number_served))        #Print Default/Initial number of customer served
    restaurant.number_served = 30                                   #Set the number_served to 30
    print('Number Served (changed): ' + str(restaurant.number_served))      #Print the changed number of customer served

    restaurant.set_number_served(40)                    #Set the number of customer served after using the method set set_number_served
    print('Number Served (After set_number_served(40)): ' + str(restaurant.number_served))

    restaurant.increment_number_served(10)              #Set the increment value, then add it to the current value
    print('Number Served (After increment_number_served(10)): ' + str(restaurant.number_served))

    restaurant.describe_restaurant()
    restaurant.open_restaurant()
except Exception as e:              #Handles the Error
    print('\nError Found...')