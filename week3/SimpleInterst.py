#Write a program to find the simple interest.
principalAmount=int(input("Enter Principal Amount: "))
interestRate=float(input("Enter Interest Rate: "))
noOfYears=float(input("Enter number of Years: "))
simpleInterest=(principalAmount*interestRate*noOfYears)/100
print("Simple Interest is: ",simpleInterest)