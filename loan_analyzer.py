import csv
from pathlib import Path

# Loan prices to be analyze
loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
loan_total = sum(loan_costs)
average_loan = sum(loan_costs) / len(loan_costs)

if(number_of_loans > 1):
  print(f"Analyzing {number_of_loans} loans for a total value of ${loan_total}. Average loan amount ${average_loan}")
elif (number_of_loans == 1): 
  print(f"Analyzing loan for a total value of ${loan_total}. Average loan amount ${average_loan}")
else: 
  print(f"No loans to be Analyzed")


# Test loan data for calculating the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Discount Rate
annual_discount_rate = 0.20

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
cost = loan.get("loan_price")

present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months

if present_value >= cost:
  print("Yes, the loan is worth at least the cost to buy it.")
else:
    print("No, the loan is too expensive and not worth the price.")
