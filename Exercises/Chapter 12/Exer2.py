#Guian Jaundell R. Manalo
#CPE3B
#Lesson 12 Exercise 2

import csv      #Import csv module to handle CSV file operations

try:        #Handle potential errors during file operations
    with open('Python/Chapter 12/guest_book.csv') as records:         #Open 'guest_book.csv' in read mode
        csv_reader = csv.reader(records)        #Create a CSV reader to read rows from the file
        for line_row, line in enumerate(csv_reader,1):      #Loop through each row in the CSV file, using enumerate to get row number
            if line_row == 1:       #Check if this is the first row
                print('Header: ')
                print(line)
                print('Data: ')
            else:               #The rows
                if line:            #Check if the row is not empty
                    print(line)     #Print all data row in the file
except Exception as e:          #Check and Catch other errors
    print('\nError Found...')
    print('Exiting Program...')