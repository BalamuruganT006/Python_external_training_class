"""
 SYNTAX

  for variable in sequence:
    # block of code
"""

#type 1

for i in range (1,1001):
    print(i)


for i in range (1,6):
    print(i)  


#type 2

for i in range (2,11,2):  #start/end/step values
    print(i)


#type 3 

for i in  range (10,0,-1):
    print(i)   


#task 4

sum=0
n=int(input("enter the numer"))
for i in range(1,n+1):
    
    sum += i    
print(sum)    


n=int(input("enter the table num: "))
r=int(input("enter the how many steps"))
for i in range (1,r+1):
    print(i,'X',n,'=',i*n)

#interview

#method 1

i=input("enter the string : ")
count=0
for j in range(0,len(i)):
    if i[j] in ['A','E','I','O','U','a','e','i','o','u']:
           count +=1
print(count)           

#method 2

i=input("enter the string : ")
count=0
for j in i:
    if j in ['A','E','I','O','U','a','e','i','o','u']:
           count +=1
print(count)   


#reverse the num without negative indexing

i=input("enter the string: ")
rev=''
for j in i:
    rev = j + rev
print(rev)    


#factorial

n=int(input("enter the num: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0 or n == 1:
    fact = 1
else:
    fact = 1
    for i in range(2, n+1):
        fact = fact * i

print(fact)    


#palindrome

i=input("enter the string: ")
rev=''
for j in i:
    rev = j + rev
if i == rev:
    print("Palidrome")
else:
    print("Not a palindrome")        
print(rev) 


# Print  A-Z
for i in range(65,91,1):
    print(chr(i), end=' ')  


#print a-z
for i in range(97,123,1):
    print(chr(i), end=' ')  


    