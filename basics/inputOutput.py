"""
#Output function in python is PRINT() function
print()
print("Hello")
print("All the power is within you")
print("All the power \nis within you") # Multi line print

a,b=10,20
print(a,b,sep='++++') # Seperator in output

Name = 'John'
marks = 95.5

#Passing variable value in print fucntion
print('Name is',Name, 'Marks are',marks)
print("Name is %s,Marks are %f"%(Name,marks))
print("Name is {},Marks are {}".format(Name,marks))
"""

#-------------------------------------------------------------------------

""" Input function used to get value from the user from the console"""

s=input("Enter your name:")
print(s)
i = int(input("Enter number:")) #By default anything passed in input is STRING, we can typecast it to any data type that we want
print(i)

print(input("Input three numbers separated by coma:").split(','))
