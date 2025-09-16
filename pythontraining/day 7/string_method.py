original_text = "Valthukal valthukal"


uppercase_text = original_text.upper()
print(uppercase_text)

print()

print(original_text)


i=input("enter the string : ")
vcount=0
ccount=0


for j in i:
    if j.isalpha() :
        if j in ['A','E','I','O','U','a','e','i','o','u']:
           vcount +=1
        else:
            ccount+=1

print(vcount)               
print(ccount)

print(i.title())


print(i.replace(" ", ""))




words = i.split()  #["python", "is ", " language"]

longest_word = max(words,key=len)
print(longest_word)


#anagram
s1 = input("enter the string:")
s2 = input("enter the string:")

if sorted(s1) == sorted(s2):
    print("anagrams")
else:
    print("not anagrams")

#print the duplicate character only using string method

s=input("enter the string:")
duplicates = ""

for ch in s:
    if ((ch != " " ) and (s.count(ch)>1 ))and (ch not in duplicates):
        duplicates += ch

print(duplicates)

s=input("enter the string")
vowels="AEIOUaeiou"
output=""
for ch in s:
    if ch in vowels:
        output += "*"
    else:
        output += ch
print(output)                   

