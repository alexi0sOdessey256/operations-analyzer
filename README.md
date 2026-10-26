# Operations Performance Analyzer
A Python-based tool that analyzes employee call resolution performance using CSV data.

This Project was built to practice applying pythonto a real-world operations scenario, including data processing, performance calculations, reporting, and basic data analysis.

## Project Overview
The Operations Performance Analyzer reads employee call data from a CSV file and generates an operational performane report.

For each employee, the program clculates:
- Unresolved calls
- Resolution rate
- Performance rating

The program also calculates team-wide metrics and identifies the highest performing employees.

## What I Learned
Through this project, I practiced:
* Variables and data types
* Conditional statements
* Loops
* Lists and dictionaries
* Functions
* CSV file processing
* File paths
* Data calculations
* Basic data analysis
* Git version control
* GitHub repository management

## Example Data

The program uses a CSV file containing:

| Employee | Calls | Resolved |

|---|---:|---:|

| Jack | 120 | 96 |

| Sarah | 150 | 135 |

| Mike | 100 | 72 |

| David | 130 | 117 |

## Features

- Reads employee data from a CSV file
- Calculates Individual resolution rates
- Calculates unresolved calls
- Assigns performance ratings
- Calculates team-wide performance
- Identifies top-performing employees
- Handles ties between top performers

## Technologies Used

- Python 3
- CSV
- VS Code
- Git
- GitHub

## How to Run

1. Clone the repository.
2. Open the project folder in VS Code.
3. Make sure 'employee.csv' is in the same folder as 'main.py'.
4. Run the program with:
'''bash
python3 main.py

## Example Output

'''text
Team Performance Report
=======================

Jack - 24 unresolved - 80.0 % - Good
Sarah - 15 unresolved - 90.0 % - Excellent
Mike - 28 unresolved - 72.0 % - Needs Improvement
David - 13 unresolved - 90.0 % - Excellent

Team Performance Summary
========================

Total calls: 500
Total resolved: 420
Total unresolved: 80

Overall resolution rate: 84.0 %

Top performers: Sarah, David
Top resolution rate: 90.0 %