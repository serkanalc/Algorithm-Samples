z = 100
# Use List Comprehension for less code
x= sum(i for i in range(1,z+1))
y= sum(i**2 for i in range(1,z+1))

print(x**2- y)
