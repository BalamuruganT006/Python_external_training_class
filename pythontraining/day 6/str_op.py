
 s=''
 print(s)


#type 2
p='s'
print(p)


#type 3
p="python"
print(p)

#type 4
s='''
      python
      java 
      c
    '''
print(s) 

#type 5
s=str(99.9)
print(s)
print(type(s))

#escape sequence/character 

print( 'Pratice makes \'prefect\' '  )



print("\"Pratice\" makes 'perfect")

#string representation

p="python"

for i in p:
    print(i)


p1='Hello'
p2='world'
print(p1[3])
print(p2[3])

print(id(p1))
print(id(p2))

print(id(p1[3]))
print(id(p2[3]))
print(id(p1[2]))


s1 = "balamurugan"
s2 = "balamurugan"

print(s1, s2) 

print(id(s1), id(s2))# address of str 

print(s1[2], s1[3], s2[3])

print(id(s1[2]), id(s1[3]), id(s2[3]))


print(s1[4], s2[1])# all the o's

print(id(s1[4]), id(s2[1]))



# STRING SCLICING 

s="python"
i=0
print( s[i : len(s) : 1])

print(s[5:3:-1])


s=input("enter the name: ")

#type 1

print(s[0:3:1])
print(s[1:4:1])
print(s[2:5:1])

#type 2  using(loop)

for i in range(0, len(s) - 2):
    k = ''
    for j in range(i, i + 3):
        k += s[j]
    print(k)


#type 3 (using indexing)
for i in range(len(s)-2):

     k = s[i:i+3]
       
     print(k)    
#print without first and last
k=s[1:-1:1]
print(k)



#reverse without fist and last
k=s[-2:0:-1]
print(k)


#srting first staight and second half as reverse

h= len(s) // 2
first = s[:h]
second = s[h:]
print(first + second[::-1])

#string comparision


s1='python'
s2='Python'

if(s1 == s2):
    print("both are same")
else:
    print("both are different")


s1='python'
s2='Python'

if(id(s1) == id (s2)):
    print("both are same")
else:
    print("both are different") 



s1='python'
s2='python'

if s1 is s2 :
    print("both are same")
else:
    print("both are different")        