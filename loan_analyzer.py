import csv
from pathlib import Path

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
  '''Calculate the present value'''
  present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
  return present_value

def write_loans_to_report(file, loans_to_write):
  '''Wrie loan report to file'''
  # Report Path
  output_path = Path(file)
  headers = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

  with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(headers)
    for loan in loans_to_write:
      csvwriter.writerow(loan.values())
  return 0

def analyze_loans(loans, annual_discount_rate):
  '''Analyze loan - print cost summary; compare present value; write to inexpensive loan report'''
  loan_costs = [loan.get('loan_price') for loan in loans ]

  number_of_loans = len(loan_costs)
  loan_total = sum(loan_costs)
  average_loan = sum(loan_costs) / len(loan_costs)

  # Print Loan Summary
  if(number_of_loans > 1):
    print(f"Analyzing {number_of_loans} loans for a total value of ${loan_total}. Average loan amount ${average_loan}")
  elif (number_of_loans == 1): 
    print(f"Analyzing loan for a total value of ${loan_total}. Average loan amount ${average_loan}")
  else: 
    print(f"No loans to be Analyzed")

  # list for target loans
  inexpensive_loans = []
  loans_to_buy = []
  loan_count = 0

  # gather loans less than 500 in inexpensive_loans
  for loan in loans:
    # increase current loan count
    loan_count = loan_count + 1
  
    # check for inexpensive loan
    if loan["loan_price"] <= 500:
      inexpensive_loans.append(loan)

    # calculate present value
    future_value = loan.get("future_value")
    remaining_months = loan.get("remaining_months")
    cost = loan.get("loan_price")

    present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate) 

    if present_value >= cost:
      print(f"Yes, loan number {loan_count} is worth at least the cost to buy it.")
      loans_to_buy.append(loan)
    else:
        print(f"No, loan number {loan_count} is too expensive and not worth the price.")

  print(f"The inexpensive loans are: {inexpensive_loans}")
  # write inexpensive loan report
  write_loans_to_report("inexpensive_loans.csv", inexpensive_loans)
  # write loans tto buy report
  write_loans_to_report("loans_to_buy.csv", loans_to_buy)

  return 0

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


analyze_loans(loans, annual_discount_rate=0.20)
