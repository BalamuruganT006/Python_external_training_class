"""l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[0][2])

l=[[1,2,3],[4,5,6],[7,8,9],(1,2,3)]

print(l[3])


l=[[1,2,3],[4,5,6],[7,8,9],(1,2,3),{12,22,32}]

print(l[4])




l=[[1,2,3],[4,5,6],[7,8,9],(1,2,3),{12,22,32},{1:'a',2:'b'}]

print(l[5][1])"""
"""
l1=[10,20,30,40,50]
l2=[60,70,80,90]"""

"""l3=l1+l2
print(l3)



l3=l1*6
print(l3)"""

"""print(l1[0:3:1])"""
"""
lst=list(map(int,input().split()))
print(lst)

"""
"""
l=[[1,2,3],[4,5,6],[7,8,9]]

print(l[0:len(l):1][-1:0:-1])"""


"""n=int(input("enter the lenth"))
l1=[]
for i in range (0,n) :
    lst=input()
    l1=l1+lst.split()
    #l1.append(lst)
print(l1)    """

"""
n = int(input())
for i in range(0,n):
        if 1<= n <= 20:
            print(i**2)"""
"""
lst = []
n = int(input())
for _ in range(n):
    p = input().split()
    c, a = p[0], list(map(int, p[1:]))
    if c == "print":
        print(lst)
    elif c == "insert":
        lst.insert(a[0], a[1])
    elif c == "remove":
        if a[0] in lst:
            lst.remove(a[0])
    elif c == "append":
        lst.append(a[0])
    elif c == "sort":
        lst.sort()
    elif c == "pop":
        if lst:
            lst.pop()
    elif c == "reverse":
        lst.reverse()"""


#append
"""l1=[10,20,30,40,50]
l2=l1+[60,70,80,90]       
l1.append(l2)
print(l1)

print(l1)        """
"""
#extends
l1=[10,20,30,40,50]
l2=[60,70,80,90] 
l1.extend(l2)
print(l1)

l1 [0] = 1111
print(l1)

l1.remove(20)
print(l1)"""



l1=[10,20,999,40,40,40,50,999,60,70,999]


#n=int(input("enter the num to remove: "))
"""for i in l1:
     if i == n :
        l1.remove(i)"""

"""# method 2
print(l1)  
while n in l1:
        l1.remove(n)    
print(l1)        """
"""print(l1)
l1.pop()
print(l1)"""

"""l2=[]  #copy(),l2=l1[:],list(l1)
l2.extend(l1)
print(l2)
print(id(l1))
print(id(l2))"""

#to fin max and min and sum both value
l1=[10,20,999,40,40,40,50,999,60,70,999]

if  l1:
    max=l1[0]
    min=l1[0]
    total=0
    for i in l1:
        if i > max:
            max = i
        if i < min:
            min = i
    total=max+min
    print("MAX:",max)
    print("MIN:",min)
    print("Total:",total)

