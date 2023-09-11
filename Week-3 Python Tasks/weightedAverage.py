writtenTest=float(input("Enter marks in written test:"))
labExam=float(input("Enter marks in Lab exam:"))
assignments=float(input("Enter marks in assignments:"))
overall=writtenTest*0.7+labExam*0.2+assignments*0.1
print("Overall marks:",round(overall,2))