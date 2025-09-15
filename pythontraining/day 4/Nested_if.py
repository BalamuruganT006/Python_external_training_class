'''
    syntax
if condition 1:
    if condition 2:
        block of code
    else:
       block of code
else: 
    block of code       
    
    '''

n=int(input("enter a num : "))

if n >= 0 :
    print("the num is positive")
    if n % 2 == 0:
        print("the given number is Even")
    else:
        print("the given number is Odd")    
else:
    print('Negative')  
    if n % 2 == 0:
        print("the given number is Even")
    else:
        print("the given number is Odd")   


x=int(input('age:'))

if x < 20:
   print('young')
   if x >= 18:
    print("you are eligible to vote ")
   else:
    print('you are not eligible') 



a=100
b=200
c=200

if a > b:
    if a > c :
        print("a is greater ")
    else:
            print('c is greater')
else:
    if b > c :
        print('b is greater')   
    else:
        if b < c : 
          print('c is greater')                             
        else:
            print('all are equal')   


age=int(input("enter the age: "))
mark=int(input('mark: '))
nationality=input('enter your natonality: ')
att=float(input('enter the attenece precentage: '))
proj=int(input('enter the no of project: '))
bonus=46
snum=int(input("enter the special number: "))

if age >= 18:
    if nationality == "INDIAN" or nationality == "indian" or nationality == "Indian":
        if mark >= 85:
            if att >= 80:
                if proj >= 5:
                    if ((mark + att) > 170) and ((proj + bonus) > 50):
                        print("you get the Mega Scholarship")
                    else:
                        print("you get the Scholarship")

                    if snum % 2 == 0:
                        if snum % 3 == 0:
                            if snum // 6 == 7:
                                if snum % 7 != 0:
                                    print("satisify")
                                else:
                                    print("not satisify")
                            else:
                                print()
                        else:
                            print()
                    else:
                        print()
                else:
                    print("Not eligible: must have completed at least 5 projects")
            else:
                print("Not eligible: attendance must be >= 80%")
        else:
            print("Not eligible: marks must be >= 85")
    else:
        print("Not eligible: must be a citizen")
else:
    print("Not eligible: age must be at least 18")


