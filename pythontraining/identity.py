x=[1,2,3]
y=[1,2,3]
z=x

print(x is y)  # differ memory address

print(x is z)  #same memory address

a="python"  #it has two reference 
b="Python"
c=a

print(id(a))
print(id(b))

print(a is not b )

print(a is b)