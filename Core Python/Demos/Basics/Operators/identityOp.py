### Identity Operator

x=10 # int is immutable, cannot change
y=10
z=20

li1=[10,20,30] # list is mutable, can change
li2=[10,20,30]

#1 is
# Check both variables refer to same memory location
print(x is y)

print(id(x))
# Return memory address of x

print(id(y))
# Return memory address of y


print(li1 is li2)
# Check both lists refer to same object

print(id(li1))
# Return memory address of li1

print(id(li2))
# Return memory address of li2


#2 is not
# Check both variables refer to different objects
print(li1 is not li2)

print(x is not y)
