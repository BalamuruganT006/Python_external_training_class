#use to create a calculator  using multiple user define functions 
def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b
def mod (a,b):
    return a%b

    
def square (a):
    return(a*a)

print("1.ADD,2.SUB,3.MULT,4.DIV,5.SQ,6.MOD")


calc=int(input("enter your choice: ") )  



match calc:
    case 1:
        x=int(input("enter the num to add 1: "))
        y=int(input("enter the num to add 2: "))
        print(add(x,y))

    case 2:
         x=int(input("enter the num  1: "))
         y=int(input("enter the num  2: "))
         print(sub(x,y))
    
    case 3:
        x=int(input("enter the num  1: "))
        y=int(input("enter the num  2: "))
        print(mul(x,y))
    
    case 4:
        x=int(input("enter the num  1: "))
        y=int(input("enter the num  2: "))
        print(div(x,y))

    case 5:
        x=int(input("enter the num  1: "))
        y=int(input("enter the num  2: "))
        print(square(x))

        print(square(y))

    case 6:
        x=int(input("enter the num  1: "))
        y=int(input("enter the num  2: "))
        print(mod(x,y))
    
    case _:

    
        print("enter the valid choice")



        
