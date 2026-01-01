#Guian Jaundell R. Manalo
#CPE3B
#Lesson 12 Exercise 3

import csv      #Import csv module to handle CSV file operations

fieldnames = ['name', 'area', 'country_code2','country_code3']      #Define the column headers for the CSV file
rows = [            #List of dictionaries, each contains a row of data for ASEAN countries
    {'name' : 'Brunei', 'area' : 5765 , 'country_code2' : 'BN', 'country_code3' : 'BRN'},
    {'name' : 'Cambodia', 'area' : 181035 , 'country_code2' : 'KH', 'country_code3' : 'KHM'},
    {'name' : 'Indonesia', 'area' : 1904569 , 'country_code2' : 'ID', 'country_code3' : 'IDN'},
    {'name' : 'Laos', 'area' : 236800 , 'country_code2' : 'LA', 'country_code3' : 'LAO'},
    {'name' : 'Malaysia', 'area' : 330803 , 'country_code2' : 'MY', 'country_code3' : 'MYS'},
    {'name' : 'Myanmar', 'area' : 676578 , 'country_code2' : 'MM', 'country_code3' : 'MMR'},
    {'name' : 'Philippines', 'area' : 300000 , 'country_code2' : 'PH', 'country_code3' : 'PHL'},
    {'name' : 'Singapore', 'area' : 736 , 'country_code2' : 'SG', 'country_code3' : 'SGP'},
    {'name' : 'Thailand', 'area' : 513120 , 'country_code2' : 'TH', 'country_code3' : 'THA'},
    {'name' : 'Vietnam', 'area' : 331690 , 'country_code2' : 'VN', 'country_code3' : 'VNM'},
]

try:        #Handle potential errors during file operations
    with open('asean_countries.csv', 'w', encoding='UTF8', newline='') as asean_info:       # Open 'asean_countries.csv' in write mode
        writer = csv.DictWriter(asean_info, fieldnames=fieldnames)          #Create a DictWriter object to write dictionaries
        writer.writeheader()        #Write the header row to the CSV file based on fieldnames
        writer.writerows(rows)      #Write all rows from the list of dictionaries to the CSV file
    print("CSV file Created Successfully.")
except Exception as e:          #Check and Catch other errors
    print('\nError Found...')
