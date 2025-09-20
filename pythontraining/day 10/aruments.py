

#[postional arumenr]

def power(a,b):
    c=a**b
    print(c)

power(2,5) # op[32]
power(5,2) #op[25]



def mul (a,b,c):
    d = a+b*c
    print(d) 

mul(1,2,3)
mul(3,2,1)
mul(3,1,2)

# default arugment

#parameter without a default follows parameter with a default

def power(a,b,c=2):
    d=a*b*c
    print(d)

power(2,3,4) 


#  [keyword arugment]

def power(a,b,c):
    d=a*b*c
    print(d)

power(a=2,b=3,c=4) 

#variable length arg
 
def pizza_toppings(*toppings):
    print(toppings)


pizza_toppings("cheese","onions","olives")



#variable keyword arg

def student(**data):
    print(data)


student(name="bala",age=21,add="tiruchengode")