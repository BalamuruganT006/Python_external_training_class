from tkinter import E


print("secure connection has been enabled: ")
try:
    p=int(input("enter te principle amount: "))
    r=8.4
    t=int(input("enter te time: "))
   
except:
    print("please enter the correct data")

else:
     si=(p*r*t)/10
     print(si)
print("secure connection has been terminated")





lst=[10,20,30,40,50,60]
d={1:"c",2:"c++",3:"pyton",4:"java"}
try:
    n=int(input("enter the key"))
    print(d[n])
    nu = int(input())
    print(lst[nu])
    den = int(input())
    print(lst[den])
    ans = lst[nu]/ lst[den]
    print(ans)
except KeyError as e:  #specific handler
    print(e)

except IndexError as e :
    print(e)

except ZeroDivisionError as e:
    print(e)


except Exception as e :
    print(e)

except :              #generic handler
    print("some issuse")
print("Execution end")


def fun2():
    print("start")
    num=int(input())
    den=int(input())
    ans=num/den
    print(ans)
    print('end')


def fun1():
    print("start 1")
    fun2()
    print("end 1")


def main():
    print('start main')
    fun1()
    print("end main")


main()