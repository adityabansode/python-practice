"""Program to remove duplicates from a list"""

l1 = eval(input("Enter a list of elements"))
print(l1)
l2=[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)

"""Approach using SET()"""

l1 = eval(input("Enter a list of elements"))
s1 = set(l1)
print(s1)