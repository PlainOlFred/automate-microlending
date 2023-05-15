import csv
from pathlib import Path

# Loan prices to be analyze
loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
loan_total = sum(loan_costs)
average_loan = sum(loan_costs) / len(loan_costs)

if(number_of_loans > 1):
  print(f"Analyzing {number_of_loans} loans for a total value of ${loan_total}. Average loan amount {average_loan}")
elif (number_of_loans == 1): 
  print(f"Analyzing loan for a total value of ${loan_total}. Average loan amount {average_loan}")
else: 
  print(f"No loans to be Analyzed")
