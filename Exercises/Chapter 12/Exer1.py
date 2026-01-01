#Guian Jaundell R. Manalo
#CPE3B
#Lesson 12 Exercise 1

import csv      #Import csv module to handle CSV file operations
import datetime     #Import datetime module to get current date and time
try:        #Handle potential errors during file operations
    with open('Python/Chapter 12/guest_book.csv', 'w') as records:        #Open 'guest_book.csv' in write mode 'w' to create or overwrite the file
        writer = csv.writer(records)        #Create a CSV writer object to write rows to the file
        header = ['Date','Guest Name']
        writer.writerow(header)     #Define Header
        while True:     #Loop to continuously prompt for guest names
            try:
                name = input('Name: ').title()      #Ask the user for their name then capitalize the first letter
                if name != '':          #Check if the input is not empty
                    if name.isdigit():      #Check if input consists of digits/numbers
                        print('\nINVALID!!! Input should not be numbers.\n')
                    elif name == 'Quit':        #Check if the input is Quit
                        print('\nExiting Program...')
                        print('Thank You...')
                        break       #Exit the loop when input is Quit
                    else:       #Input is Valid
                        print('Hello ' + name + '! Welcome!\n')
                        date = datetime.datetime.now().strftime("%B-%d-%y %I:%M:%S %p")     #Get current Date and Time
                        writer.writerow([date,name])        #Write the date and name as a new row in the CSV File
                else:
                    print('\nINVALID!!! Input cannot be empty.\n')
            except ValueError:      #Catch if their is an error occur in input process
                print('\nError Found...\n')
except Exception as e:          #Check and Catch other errors
    print('\nError Found...')
    print('Exiting Program...')
