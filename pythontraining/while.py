"""
    SYNTAX

    while condition:
        #block of code

"""


i = 0
while i < 10:
    i+=1
    print(i)      
while (True):

      i=input("enter a key :")
      if (i == 'k') or (i == 'K') :
        break
    


#while using list
l=['apple','banana','mango','orange','blueberry'] 
i = 0
while i < len(l):
    print(l[i])
    i += 1


i = 0
while i < 10:
    if i == 5:
        break
    print(i) 
    i+=1


i = 0
while i < 10:
    i+=1
    if i == 5:
        continue
    print(i) 
    

i = 0
while i < 10:
    i+=1
    if i == 5:
        pass
    print(i)    
   


i=int(input('enter the num: '))
dig = str(i)
j=0
sum=0

while j < len(dig):
    sum += int(dig[j])
    j += 1
print(sum)    