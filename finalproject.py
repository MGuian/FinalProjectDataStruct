#Final Project
import pandas as pd

df = pd.read_csv("Collisions_Crashes.csv")
df["CRASH DATE"] = pd.to_datetime(df["CRASH DATE"], format="%m/%d/%Y", errors="coerce")
filtered = df[df["CRASH DATE"].dt.year == 2024].copy()
filtered["MONTH"] = filtered["CRASH DATE"].dt.month

total_injured = filtered["NUMBER OF PERSONS INJURED"].sum()
total_killed = filtered["NUMBER OF PERSONS KILLED"].sum()

greatest_street = filtered["ON STREET NAME"].value_counts().idxmax()
greatest_street_count = filtered["ON STREET NAME"].value_counts().max() 

greatest_vehicle = filtered["VEHICLE TYPE CODE 1"].value_counts().idxmax()
greatest_vehicle_count = filtered["VEHICLE TYPE CODE 1"].value_counts().max() 

top5_streets = filtered["ON STREET NAME"].value_counts().head(5) 

top5_vehicles = filtered["VEHICLE TYPE CODE 1"].value_counts().head(5)

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

greatest_month = filtered["MONTH"].value_counts().idxmax()
greatest_month_count = filtered["MONTH"].value_counts().max()

greatest_month_value = month[greatest_month - 1]

# Changed to get top 5 months by count (already sorted descending), then rename to month names
top5_months = filtered["MONTH"].value_counts().head(5)
top5_months_value = top5_months.rename(index=lambda x: month[x-1])

print("\n-----------------------------------------------------------")
print("Collision Crashes Analysis 2024")
print("-----------------------------------------------------------")
print("Total Injured: " + str(total_injured))
print("Total Killed: " + str(total_killed))
print("The Greatest Street: " + (greatest_street) + " \tTotal Count: " + str(greatest_street_count))
print("The Greatest Month: " + (greatest_month_value) + " \t\tTotal Count: " + str(greatest_month_count))
print("The Greatest Vehicle: " + (greatest_vehicle) + " \t\tTotal Count: " + str(greatest_vehicle_count))
print("-----------------------------------------------------------")
print("Top 5 Streets:")
print(top5_streets)
print("-----------------------------------------------------------")
print("Top 5 Vehicles:")
print(top5_vehicles)
print("-----------------------------------------------------------")
print("Top 5 Months:")
print(top5_months_value)
print("-----------------------------------------------------------")

# Prepare data for CSV, including top 5 months with names
Data_Analysis = {
    "Analysis": [
        "Total Injured", "Total Killed", "Greatest Street", "Greatest Street Count", 
        "Greatest Month", "Greatest Month Count", "Greatest Vehicle", "Greatest Vehicle Count"
    ],
    "Data": [
        total_injured, total_killed, greatest_street, greatest_street_count,
        greatest_month_value, greatest_month_count, greatest_vehicle, greatest_vehicle_count
    ]
}

data_records = pd.DataFrame(Data_Analysis)

data_records.to_csv("records.csv", index=False)
print("\nGathered Data has been saved to 'records.csv'")