#Final Project
#Data Structure

import pandas as pd
from sys import exit

# ======================================================
# CONFIGURATION
# ======================================================

FILE_PATH = "Motor_Vehicle_Collisions_-_Crashes_20251218.csv"
TARGET_YEAR = 2024

# ======================================================
# DATA LOADING & CLEANING
# ======================================================

def load_collision_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        engine="python",
        on_bad_lines="skip"
    )

    # Normalize column names
    df.columns = (
        df.columns
        .str.replace('"', '', regex=False)
        .str.strip()
        .str.lower()
    )

    # Convert date column
    df["crash date"] = pd.to_datetime(
        df["crash date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    return df


def filter_by_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    filtered = df[df["crash date"].dt.year == year].copy()

    if filtered.empty:
        print(f"No data available for year {year}")
        print("Years found:")
        print(df["crash date"].dt.year.value_counts().sort_index())
        exit()

    filtered["month"] = filtered["crash date"].dt.month
    return filtered


# ======================================================
# ANALYTICS
# ======================================================

def compute_statistics(df: pd.DataFrame) -> dict:
    return {
        "injured_total": df["number of persons injured"].sum(),
        "killed_total": df["number of persons killed"].sum(),

        "top_street": df["on street name"].value_counts().idxmax(),
        "top_street_count": df["on street name"].value_counts().max(),

        "top_vehicle": df["vehicle type code 1"].value_counts().idxmax(),
        "top_vehicle_count": df["vehicle type code 1"].value_counts().max(),

        "top_month": df["month"].value_counts().idxmax(),
        "top_month_count": df["month"].value_counts().max(),

        "top5_streets": df["on street name"].value_counts().head(5),
        "top5_vehicles": df["vehicle type code 1"].value_counts().head(5),
        "top5_months": df["month"].value_counts().sort_index().head(5)
    }


# ======================================================
# DISPLAY FUNCTIONS
# ======================================================

def print_summary(stats: dict):
    width = 48
    print("\nAnalysis Description".ljust(width) + "Result")
    print("-" * (width + 12))

    rows = [
        ("Total Injured Persons (2024)", stats["injured_total"]),
        ("Total Fatalities (2024)", stats["killed_total"]),
        ("Most Accident-Prone Street", stats["top_street"]),
        ("Accidents on That Street", stats["top_street_count"]),
        ("Most Involved Vehicle Type", stats["top_vehicle"]),
        ("Accidents Involving That Vehicle", stats["top_vehicle_count"]),
        ("Month With Most Accidents", stats["top_month"]),
        ("Accidents During That Month", stats["top_month_count"]),
    ]

    for label, value in rows:
        print(label.ljust(width) + str(value))


def print_top(title: str, series: pd.Series, label_prefix=""):
    print(f"\n--- {title} ---")
    for key, val in series.items():
        print(f"{label_prefix}{str(key).ljust(40)} {val}")


def export_report(stats: dict):
    report = pd.DataFrame({
        "Analysis Description": [
            "Total Injured Persons (2024)",
            "Total Fatalities (2024)",
            "Most Accident-Prone Street",
            "Accidents on That Street",
            "Most Involved Vehicle Type",
            "Accidents Involving That Vehicle",
            "Month With Most Accidents",
            "Accidents During That Month"
        ],
        "Result": [
            stats["injured_total"],
            stats["killed_total"],
            stats["top_street"],
            stats["top_street_count"],
            stats["top_vehicle"],
            stats["top_vehicle_count"],
            stats["top_month"],
            stats["top_month_count"]
        ]
    })

    report.to_csv("NYC_Collision_Final_Report_2024.csv", index=False)
    print("\nCSV report exported successfully.")


# ======================================================
# MENU SYSTEM
# ======================================================

def show_menu():
    print("\n===== NYC COLLISION ANALYSIS (2024) =====")
    print("1. Injury and fatality summary")
    print("2. Most accident-prone street")
    print("3. Most involved vehicle type")
    print("4. Month with most accidents")
    print("5. Full summary + export CSV")
    print("6. Top 5 streets")
    print("7. Top 5 vehicles")
    print("8. Top 5 months")
    print("9. Exit")


# ======================================================
# MAIN EXECUTION
# ======================================================

df_raw = load_collision_data(FILE_PATH)
df_2024 = filter_by_year(df_raw, TARGET_YEAR)
stats = compute_statistics(df_2024)

actions = {
    "1": lambda: print(f"\nInjured: {stats['injured_total']}\nKilled: {stats['killed_total']}"),
    "2": lambda: print(f"\n{stats['top_street']} — {stats['top_street_count']} accidents"),
    "3": lambda: print(f"\n{stats['top_vehicle']} — {stats['top_vehicle_count']} accidents"),
    "4": lambda: print(f"\nMonth {stats['top_month']} — {stats['top_month_count']} accidents"),
    "5": lambda: (print_summary(stats), export_report(stats)),
    "6": lambda: print_top("Top 5 Accident-Prone Streets", stats["top5_streets"]),
    "7": lambda: print_top("Top 5 Vehicle Types", stats["top5_vehicles"]),
    "8": lambda: print_top("Top 5 Months", stats["top5_months"], label_prefix="Month "),
}

while True:
    show_menu()
    choice = input("\nSelect an option (1-9): ").strip()

    if choice == "9":
        print("\nProgram exited successfully.")
        break

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid selection. Please try again.")
