# automate-microlending

## Description
Determine which loans that will likely return. Program generate loans to buy and inexpensive loan reports. Loans to buy are calcuate base on the present value of loan. Inexpensive loans are based on a buy thershold.

## Usage 
1. Enter list of loans in format
```python
loans = [
  {
    "loan_price": number,
    "remaining_months": number,
    "repayment_interval": "monthly" | "bullet",
    "future_value": number,
   }
]
```

2. Run Program 
 <br>program assumes annual discount rate of 0.20
