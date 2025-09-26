def power(a,b):
    c=a**b
    print(c)

power(2,3) 

c=(lambda a,b : a**b) (2,3)
print(c)

fun= (lambda a,b : a**b)
ans = fun(10,2)
print(ans)

n=int(input("enter the num: "))
ch=(lambda a : print(a))
if (n % 2 == 0):
    ch(n)
    print("is even")
else:
    ch(n)
    print("is odd")    

n=input("enter the string: ")

reverse_simple = lambda s: s[::-1]
print("Reversed string:", reverse_simple(n))


# filter
l=[10,13,24,15,25,30,66]
even=[]
def fun(x):
    for i in l:
        if i % 2 == 0:
            even.append(i)
    print(even) 
fun(l)          



l=[10,13,24,15,25,30,66]

def fun(x):
    
        if x % 2 == 0:
            return True
        else:
            return False
  
c=list(filter(fun,l))
print(c)

#lambda function

l=[10,13,24,15,25,30,66]
ans=list(filter(lambda a: True if a%2 == 0 else False,l))
print(ans)

#str ,str remove,repation,reverse


#reduce
l=[1,2,3,4,5]
def fun(a):
     print("sum:", sum(a))
fun(l)

from functools import reduce

l=[1,2,3,4,5]
result = reduce(lambda x, y: x + y, l)
print("sum:", result)


from functools import reduce
l=[1,2,3,4,5]
def fun(x,y):
    return x+y
ans=reduce(lambda x,y: x+y,l)
print(ans)



l=[1,2,3,4,5]
def fun(x):
    return x**2

sq=list(map(fun,l))
print(sq)



l=[1,2,3,4,5]
ans=list(map(lambda a: a**2 ,l))
print(ans)