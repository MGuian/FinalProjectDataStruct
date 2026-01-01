#Guian Jaundell R. Manalo
#CPE3B
#Lesson 12 Exercise 4

import csv      #Import csv module to handle CSV file operations

try:        #Handle potential errors during file operations
    with open('asean_countries.csv') as asean_info:     #Open 'asean_countries.csv' in read mode
        csv_reader = csv.reader(asean_info)         #Create a CSV reader to read rows from the file
        for row in csv_reader:           #Loop through each row in the CSV file
            if row:                 #Check if the row is not empty
                print(row)          #Print all data row in the file
except Exception as e:          #Check and Catch other errors
    print('\nError Found...')
    print('Exiting Program...')


