#Guian Jaundell R. Manalo
#CPE3B
##Lesson 13 Exercise 3

class Restaurant:       #Class to represent the restaurant
    def __init__(self, restaurant_name, cuisine_type):      #Initialize the name of the restaurant and cuisine type
        self.restaurant_name = restaurant_name          #Assigning of attributes
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):          #Method to Print info of the restaurant
        print('\nRestaurant Name: ' + self.restaurant_name)
        print('Type of Cuisine: ' + self.cuisine_type)
    def open_restaurant(self):          #Method to Print the message that the restaurant is open
        print('\n' + self.restaurant_name + ' is open today.\n')
try:
    #Instance of restaurant
    restaurant = Restaurant("Pizza Hut", "Italian-American")
    #Print the restaurant_name attribute and cuisine_type attribute individually
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    #Call the describe_restaurant to print the restaurant information and open_restaurant to print that restaurant is open
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
except Exception as e:              #Handles the Error
    print('\nError Found...')