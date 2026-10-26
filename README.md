# Operations Performance Analyzer
A Python-based tool that analyzes employee call resolution performance using CSV data.

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