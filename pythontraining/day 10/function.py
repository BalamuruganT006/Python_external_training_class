#without parameter with  without return datatype
def mlt():
    a=10
    b=20
    c=a*b
    print(c)
mlt()


#with parameter with  without return datatype

def mul(x,y):
    c=x*y 
    print(c)

mul(20,46)    


#without parameter with  with return datatype


def mlt3():
    a=10
    b=20
    c=a*b
    return c

ans=mlt3()
print(ans)


#with parameter and with return datatype

def mlt3(a,b):
    c=a*b
    return c

ans=mlt3(50,75)
print(ans)