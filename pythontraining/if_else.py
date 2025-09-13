x=2000
 

if x<100:
    print("x is less than 100 ")
else:
    print("x is greater than 100")  


#task 1

m=int(input("enter the mark: "))

if m >= 90 and m <= 100: # 90- 100
    print("O")
elif m >= 80 and m <90: # 80- 89 
    print("A")
elif m >= 70 and m <80: #70 - 79
    print("B+")
elif m >= 60 and m <70:  #60 - 69
    print("B")
elif m >= 50 and m <60:  #50 - 59 
    print("C")        
else:                   #less than 50
    print("fail")            
   


#task 2

m = float(input("enter the movie rating  (out of 10):  "))

if m >= 9: 
    print("Rank-1 - Blockbuster HIT")
elif m >= 7.5 and m <9:  
    print("Rank 2- superhit")
elif m >= 6 and m < 7.5: 
    print("Rank 3-HIT")
elif m >= 4 and m < 6:  
    print("rank 4-Average")

else:                   
    print("Rank 5 - Flop") 

#task 3




#check prime number
num=int(input("Enter the number :"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break  
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


