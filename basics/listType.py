lst = [10,20,'Addy',-10,30.5]
print(lst)
print(lst[3])
print(lst[2:5])
lst.append(40)
print(lst)

lst.remove('Addy')
print(lst)

del(lst[1])
print(lst)

a = None
print(a)

def m1():
    a=10

print(m1())