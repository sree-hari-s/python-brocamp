mark = float(input("Enter total marks: "))
if mark >= 90:
	print("\nGrade:A")
elif (mark<=89 and mark>=80):
    print("\nGrade:B")
elif (mark<=79 and mark>=70):
	print("\nGrade:C")
elif(mark<=69 and mark>=60):
	print("\nGrade:D")
elif (mark<=59 and mark>=50):
	print("\nGrade:E")
else:
	print("\nFailed")