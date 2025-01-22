m = int(input("Enter marks for maths:"))
p = int(input("Enter marks for physics:"))
c = int(input("Enter marks for chemistry:"))

course = [m,p,c]
if m<35:
    print("Student has failed is maths")
elif p<35:
    print("Student has failed is physics")
elif c<35:
    print("Student has failed is chemistry")
else:
    print("Student has passed")

total_Score = m+p+c
print("Total Score is:", total_Score)

average = total_Score/3
print("Average marks of student are:",average)

if average <= 59:
    print("Student has passed with Grade C")
elif average <= 69:
    print("Student has passed with Grade B")
else:
    print("Student has passed with Grade A")
