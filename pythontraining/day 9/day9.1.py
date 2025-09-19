'''### tuple
t=(44 ,3, 35, 4)
print(t)
print(type(t))

## mixed
mixed=(1,"hello",3.14,"false")
print(mixed)

## indexing
t=(10,20,30,40,50)
print(t)
print(t[-1])
print(t[1::2])

## list to tuple
t=(10,20,30,40,50,60)
s=list(t)
print(t)
s[0]=200
s[1]=300
t=tuple(s)
print(t)

## concadition only adding
t1=(10,20,30,40,50,60)
t2=(20,30,50)
t3=t1+t2
print(t3)

## concadition using index
t1=(10,20,30,40,50,60)
t2=(20,30,50)
print(t1[0]+t2[1])

## replication
t1=(10,20,30)
t2=(20,40,50)
print(t1[0]*t2[1])

## membership
t1=("surya")
if "e" in t1:
    print("  perfect")
else:
    print(" not perfect")

## iteration
t=(10)
for i in range(0,t):
    print(i)'''

