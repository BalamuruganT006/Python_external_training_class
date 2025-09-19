'''## sorted
t=(18,46,3,6,2,7)
print(sorted(t))

## packing
t=10,20,30,40
print(t)

### unpacking
a,b,c,d=t
print(a,b,c,d)

## nested
nested=(9,(1,2,3,4),(6,7,8))
print(nested)
print(nested[1])

##palindrome
s=input("enter your words")
w=''
for i in s:
    w=i+w
print(w)
if s==w:
    print("palindrome")
else:
    print("not palindrome")

## append the list in tuple
person = ("Alice", 25, ["Python", "Java"])
print(person)

person[2].append("c")
print(person)'''