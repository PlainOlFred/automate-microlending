import csv
from pathlib import Path

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
  '''Calculate the present value'''
  present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
  return present_value

# Test loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
      "loan_price": 500,
      "remaining_months": 9,
      "repayment_interval": "bullet",
      "future_value": 1000,
  }
]
current_loan = 0


# Loan prices to be analyze
loan_costs = [loan.get('loan_price') for loan in loans ]

number_of_loans = len(loan_costs)
loan_total = sum(loan_costs)
average_loan = sum(loan_costs) / len(loan_costs)

#To hold that cost $500 or less
inexpensive_loans = []

if(number_of_loans > 1):
  print(f"Analyzing {number_of_loans} loans for a total value of ${loan_total}. Average loan amount ${average_loan}")
elif (number_of_loans == 1): 
  print(f"Analyzing loan for a total value of ${loan_total}. Average loan amount ${average_loan}")
else: 
  print(f"No loans to be Analyzed")

# Discount Rate
annual_discount_rate = 0.20


# gather loans less than 500 in inexpensive_loans
for loan in loans:
  # increase current loan count
  current_loan = current_loan + 1

  # check for inexpensive loan
  if loan["loan_price"] <= 500:
    inexpensive_loans.append(loan)

  # calculate present value
  future_value = loan.get("future_value")
  remaining_months = loan.get("remaining_months")
  cost = loan.get("loan_price")

  present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate) 

  if present_value >= cost:
    print(f"Yes, loan number {} is worth at least the cost to buy it.")
  else:
      print("No, the loan is too expensive and not worth the price.")

print(f"The inexpensive loans are: {inexpensive_loans}")

# Write inexpensive loans report 
# Report headers
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Report Path
output_path = Path("inexpensive_loans.csv")

with open(output_path, 'w') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',')
  csvwriter.writerow(header)
  for loan in inexpensive_loans:
    csvwriter.writerow(loan.values())
