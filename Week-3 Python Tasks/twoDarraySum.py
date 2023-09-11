def two_d_matrix(m, n):  
    Output = []  
    for i in range(m):  
        row = []
        for j in range(n):  
            num = int(input(f"Enter the matrix [{0}][{j}]"))
            row.append(num)  
        Output.append(row)
    return Output
def sum(A, B): 
    output = []  
    print("Sum of the matrix is :")
    for i in range(len(A)): 
        row = []
        for j in range(len(A[0])):  
            row.append(A[i][j] + B[i][j]) 
        output.append(row)
    return output   
def displayArray(A):
    for r in A:
        for c in r:
            print(c,end = " ")
        print()
m = int(input("Enter the value of m or Row\n")) 
n = int(input("Enter the value of n or columns\n")) 

print("Enter the First matrix ")  
A = two_d_matrix(m, n) 
print("display the first (A) matrix")
displayArray(A) 
print("Enter the Second (B) matrix ")
B = two_d_matrix(m, n)  
print("display the Second (B) matrix")
displayArray(B)  
s = sum(A, B) 
displayArray(s) 
