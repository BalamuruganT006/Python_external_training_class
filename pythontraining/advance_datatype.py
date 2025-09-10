


lst1=[1,2,3,4,5,6,7,8]
lst2=[9,10,11,12,13,14,15,16]
print(lst1)
print(lst2)
su=sum(lst1)+sum(lst2)
print(su)
#using lenght functon
lenght1=len(lst1)
for i in range(0,lenght1):
    sum =lst1[i]+lst2[i]
print(sum)   

#type
print(type(lst1))

#print using indexing
print(lst1[5])
#append
lst1.append(9)
print(lst1)

#insert
lst2.insert(8,17)
print(lst2)

#reverse
lst1.reverse()
print(lst1)

#concatination
lst3=lst1+lst2
print(lst3)

#replace
lst3[0]=100
print(lst3)

#delete
lst3.remove(100)
print(lst3)

#pop
lst3.pop(10)
print(lst3)

#sort
lst3.sort()
print(lst3)

#count the even numbers in list

lenght2=len(lst1)
even=0
odd=0
for i in lst1:
    if i % 2 == 0:
        even= even +1
    else:
        odd= odd +1
print('even number in list1 ' ,even )
print('odd number list2',odd)    

#count the even numbers in list with different increment
 
even=0
odd=0
for i in range(0,len(lst2)):
    if i % 2 == 0:
        even+=1
    else:
        odd+=1   
print('even number in list2 ' ,even )
print('odd number in list2',odd)

#tuple 
my=(1,2,3,4,5)
x=5

if x in my:
    print('true')
else:
    print('false')

#set 
s={1,5,3,4,2,7,8,6}
print(type(s))
print(s)
s.add(20)
print(s)
s.add(10)
s.add(200)
s.add(101)
s.add(600)
s.add(222)
s.add(754)
s.add(111)
s.add(1015)
print(s)
s.remove(10)
s.remove(200)
s.remove(101)
s.remove(600)
s.remove(222)
s.remove(754)
s.remove(111)
s.remove(1015)
print(s)

#dictionary values

dict={ "name":"bala","age":19}
print(dict["name"])
stu={"name":"arun","age":21,"branch":"cy"}
print(stu)
print(stu["age"],stu["name"])
print(type(dict))
#pop
dict.pop("name")
print(dict)
#add ne key-value pair
stu["grade"]="A"
print(stu)

#print both key and value

for i,j in stu.items():
    print(i,":",j)
    
