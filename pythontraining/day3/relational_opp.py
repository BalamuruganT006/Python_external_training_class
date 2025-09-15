#relatinal operator

x=int(input("enter the num :"))
y=int(input("entyer the num :"))

print(x==y)#check values

print(x!=y)

print(x>y)


print(x < y)

#intervew

year=int(input("enter the year:"))
if (year % 400 == 0) or ((year % 4 == 0) & (year % 100 != 0)):
 print("Leap year")
else:
    print("not a leap year")


#grater than or equal to , less than or equal to


mark=int(input("enter the num: "))
if(mark>=90 & mark<=100):
 print ("Distinction")
elif(mark>=50):
    print("Pass")
else:
    print("Fail")
