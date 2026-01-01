#Final Project
import pandas as pd         # Import pandas for data manipulation

df = pd.read_csv("Collisions_Crashes.csv")                      # Read the CSV file
df["CRASH DATE"] = pd.to_datetime(df["CRASH DATE"], format="%m/%d/%Y", errors="coerce")         # Convert the "CRASH DATE" column to datetime format
filtered = df[df["CRASH DATE"].dt.year == 2024].copy()              # Filter the DataFrame, include only rows where the year is 2024
filtered["MONTH"] = filtered["CRASH DATE"].dt.month                 # Extract the month from the crash date

# Calculate total injured and killed
total_injured = filtered["NUMBER OF PERSONS INJURED"].sum()
total_killed = filtered["NUMBER OF PERSONS KILLED"].sum()
# Determine the street with the highest number of crashes
greatest_street = filtered["ON STREET NAME"].value_counts().idxmax()
greatest_street_count = filtered["ON STREET NAME"].value_counts().max() 
# Determine the vehicle type with the highest number of crashes
greatest_vehicle = filtered["VEHICLE TYPE CODE 1"].value_counts().idxmax()
greatest_vehicle_count = filtered["VEHICLE TYPE CODE 1"].value_counts().max() 
# Get top 5 streets and vehicle types
top5_streets = filtered["ON STREET NAME"].value_counts().head(5) 
top5_vehicles = filtered["VEHICLE TYPE CODE 1"].value_counts().head(5)

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Determine the month with the highest number of crashes
greatest_month = filtered["MONTH"].value_counts().idxmax()
greatest_month_count = filtered["MONTH"].value_counts().max()
# Convert month number to month name
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

# Prepare data for CSV
analysis = [
    "Total Injured", "Total Killed", "Greatest Street", "Greatest Street Count", 
    "Greatest Month", "Greatest Month Count", "Greatest Vehicle", "Greatest Vehicle Count"
]
data = [
    total_injured, total_killed, greatest_street, greatest_street_count,
    greatest_month_value, greatest_month_count, greatest_vehicle, greatest_vehicle_count
]

# Add top 5 streets to the lists
for i, (street, count) in enumerate(top5_streets.items(), 1):
    analysis.append(f"Top Street {i}")
    data.append(f"{street}: {count}")

# Add top 5 vehicles to the lists
for i, (vehicle, count) in enumerate(top5_vehicles.items(), 1):
    analysis.append(f"Top Vehicle {i}")
    data.append(f"{vehicle}: {count}")

# Add top 5 months to the lists
for i, (month_name, count) in enumerate(top5_months_value.items(), 1):
    analysis.append(f"Top Month {i}")
    data.append(f"{month_name}: {count}")

Data_Analysis = {
    "Analysis": analysis,
    "Data": data
}

# Create DataFrame and save to CSV
data_records = pd.DataFrame(Data_Analysis)
# Save the DataFrame to a CSV file
data_records.to_csv("records.csv", index=False)
print("\nGathered Data has been saved to 'records.csv'")