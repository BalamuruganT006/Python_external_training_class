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

print(l1)        """

#extends
l1=[10,20,30,40,50]
l2=[60,70,80,90] 
l1.append(l2)
print(l1)

l1 [0] = 1111
print(l1)
