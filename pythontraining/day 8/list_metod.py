l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[0][2])

l=[[1,2,3],[4,5,6],[7,8,9],(1,2,3)]

print(l[3])


l=[[1,2,3],[4,5,6],[7,8,9],(1,2,3),{12,22,32}]

print(l[4])




l=[[1,2,3],[4,5,6],[7,8,9],(1,2,3),{12,22,32},{1:'a',2:'b'}]

print(l[5][1])


l1=[10,20,30,40,50]
l2=[60,70,80,90]

l3=l1+l2
print(l3)



l3=l1*6
print(l3)

print(l1[0:3:1])


lst=list(map(int,input().split()))
print(lst)



l=[[1,2,3],[4,5,6],[7,8,9]]

print(l[0:len(l):1][-1:0:-1])


n=int(input("enter the lenth"))
l1=[]
for i in range (0,n) :
    lst=input()
    l1=l1+lst.split()
    #l1.append(lst)
print(l1)    


n = int(input())
for i in range(0,n):
        if 1<= n <= 20:
            print(i**2)

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
        lst.reverse()


#append
l1=[10,20,30,40,50]
l2=l1+[60,70,80,90]       
l1.append(l2)
print(l1)

print(l1)       

#extends
l1=[10,20,30,40,50]
l2=[60,70,80,90] 
l1.extend(l2)
print(l1)

l1 [0] = 1111
print(l1)

l1.remove(20)
print(l1)



l1=[10,20,999,40,40,40,50,999,60,70,999]


#n=int(input("enter the num to remove: "))
for i in l1:
     if i == n :
        l1.remove(i)

# method 2
print(l1)  
while n in l1:
        l1.remove(n)    
print(l1)        

print(l1)
l1.pop()
print(l1)


l2=[]  #copy(),l2=l1[:],list(l1)
l2.extend(l1)
print(l2)
print(id(l1))
print(id(l2))

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



# ===== List methods demo =====
if __name__ == "__main__":
    # append(x): Add item to end
    base = [3, 1, 2]
    l = base.copy()
    l.append(4)
    print("append:", l)

    # extend(iterable): Add all items from iterable
    l = base.copy()
    l.extend([4, 5])
    print("extend:", l)

    # insert(i, x): Insert at index i
    l = base.copy()
    l.insert(1, 99)
    print("insert:", l)

    # remove(x): Remove first occurrence of x
    l = [1, 2, 2, 3]
    l.remove(2)
    print("remove first 2:", l)

    # pop([i]): Remove and return item at i (default last)
    l = base.copy()
    last = l.pop()
    print("pop last:", last, l)
    l = base.copy()
    first = l.pop(0)
    print("pop index 0:", first, l)

    # clear(): Remove all items
    l = base.copy()
    l.clear()
    print("clear:", l)

    # index(x[, start[, end]]): Return first index of x
    l = [10, 20, 10, 30]
    print("index of 10:", l.index(10))

    # count(x): Count occurrences of x
    print("count of 10:", l.count(10))

    # sort(*, key=None, reverse=False): In-place sort
    l = [3, 1, 2]
    l.sort()
    print("sort asc:", l)
    l.sort(reverse=True)
    print("sort desc:", l)
    l = [("a", 2), ("b", 1)]
    l.sort(key=lambda x: x[1])
    print("sort by key (2nd item):", l)

    # reverse(): In-place reverse
    l = [1, 2, 3]
    l.reverse()
    print("reverse:", l)

    # copy(): Shallow copy
    l = [1, 2, 3]
    c = l.copy()
    print("copy:", c, "is same object:", c is l)