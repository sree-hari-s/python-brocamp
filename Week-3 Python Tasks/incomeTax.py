annualIncome=float(input("Enter annual income:"))
tax=0
if annualIncome<=250000:
    tax=0
elif annualIncome>250000 or annualIncome<=500000:
    tax=0.05
elif annualIncome>500000 or annualIncome<=1000000:
    tax=0.2
elif annualIncome>1000000 or annualIncome<=5000000:
    tax=0.3
print("Income tax:",annualIncome*tax)