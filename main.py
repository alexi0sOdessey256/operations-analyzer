# Calling python code from a CSV file.
import csv

# Giving Python the tools for interacting with the CPU's OS things like files, folders, file paths, etc.
import os

def calculate_resolution_rate( calls, resolved):
    return resolved / calls * 100

# (__file__) -> Means the file which Python is currently running from.
# os.path.dirname() -> "What folder is this is inside?"
# os.path.abspath(__file__) -> "Give me the complete/absolute path to main.py"
folder = os.path.dirname(os.path.abspath(__file__))

# "Take the folder found and add employees.csv to it."
csv_file = os.path.join(folder, "employees.csv")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    #Printing the Team Performance Report.
    print("Team Performance Report")
    print("=======================")
    print()

    total_calls = 0
    total_resolved = 0
    total_unresolved = 0
    best_employees = []
    best_rate = 0
    worst_employees = []
    worst_rate = 101

    for employee in reader:
        employee["calls"] = int(employee["calls"])
        employee["resolved"] = int(employee["resolved"])
        employee["unresolved"] = employee["calls"] - employee["resolved"]
        

        total_calls += employee["calls"]
        total_resolved += employee["resolved"]
        total_unresolved += employee["unresolved"]


        resolution_rate = calculate_resolution_rate(
            employee["calls"],
            employee["resolved"]
        )

        #Loop through each employee and determine their performance based on their resolution rate.
        if resolution_rate >= 90:
            performance = "Excellent"
        elif resolution_rate >= 80:
            performance = "Good"
        else:
            performance = "Needs Improvement"

        #Output of Low and High Performance Employees.
        print(
        employee["name"],
        "-",
        employee["unresolved"],
        "unresolved",
        "-",
        round(resolution_rate, 2),
        "%",
        "-",
        performance
        )
        
        #Determine the best performing employee(s) based on their resolution rate.
        if resolution_rate > best_rate:
            best_rate = resolution_rate
            best_employees = [employee["name"]]

        elif resolution_rate == best_rate:
            best_employees.append(employee["name"])

        #Determine the worst performing employee(s) based on their resolution rate.
        if resolution_rate < worst_rate:
            worst_rate = resolution_rate
            worst_employees = [employee["name"]]

        elif resolution_rate == worst_rate:
            worst_employees.append(employee["name"])

    overall_rate = total_resolved / total_calls * 100

#Output of Team Performance Summary.
    print()
    print("Team Performance Summary")
    print("=======================")
    print()
    print("Total calls:", total_calls)
    print("Total resolved:", total_resolved)
    print("Total unresolved:", total_unresolved)
    print()
    print("Overall resolution rate:", round(overall_rate, 2), "%")
    print()
    print("Top performers:", ", ".join(best_employees))
    print("Top resolution rate:", round(best_rate, 2), "%")
    print()
    print("Lowest performers:", ", ".join(worst_employees))
    print("Lowest resolution rate:", round(worst_rate, 2), "%")
    print()