import random

print("Password Generator")
chars='abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ@#$%=:?./|~>*()<0123456789'
numbers=int(input("Number of passwords to generate:"))
length=int(input("Enter your password length:"))
print("Here are you're passwords:")
for i in range(numbers):
    passwords=''
    for j in range(length):
        passwords+=random.choice(chars)
    print(passwords)