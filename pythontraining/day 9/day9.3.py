#set

#A set is a collection of unique elements.

#Built-in data type in Python.

#Unordered, unindexed, and does not allow duplicates.


'''## set topics
s={1,2,3,3,2,4}
print(s)

s=set([1,2,2,3,4,5,3])
print(s)

s=set()
print(type(s))

s={}
print(type(s))

## loop in set
s={10,20,30}
for item in s:
    print(item)
    
## add element in list
s={1,2,3}
s.add(100)
print(s)

s.update([4,6,8,5])
print(s)

##remove element in list
s={1,2,4,3,6,5,7}
s.remove(5)
s.discard(9)
s.pop()
s.clear()
print(s)

#set operations
a={1,2,3,4,5}
b={3,9,8,6,7}
print(a|b)  #union
print(a&b)  #intersaction
print(a-b)  #difference
print(b-a)  #difference
print(a^b)  #semantic difference

## set methods
s={1,2,3,4,7,5,6}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))'''

## set types
s1={2,3,5}
s2={6,7,8}
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))

#
s=frozenset([1,2,3])
print(s)
s.add(100)
print(s)
