'''student=dict(name="alice",age=20,course="python")
print(student)

d={"a":1,"b":2,"a":3}
print(d)

## dictionary add and update
di={"name":"alice","age":20,"dept":"it"}
di["city"]="new york"
di["age"]=25
print(di)

## dictionary delete methods
di={"name":"alice","age":20,"dept":"it","city":"new york"}
di.pop("age")
di.popitem()  #delete the last element in the dictionary
del di["name"]
di.clear()
print(di)

## merge the list
di1={"name":"alice","age":20,"dept":"it","city":"new york"}
di2={"name":"sam","age":23,"dept":"csc"}
print(di1|di2)

##member ship operator
di1={"name":"alice","age":20,"dept":"it","city":"new york"}
di2={"name":"sam","age":23,"dept":"csc"}
print("name"in di1)
print("age" not in di1)

## dictionary methods
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())
print(d.values())
print(d.items())
print(d.get("a"))
print(d.setdefault("d", 0))
print(d)
d.update({"b": 5, "e": 6})
print(d)
d2 = d.copy()
print(d2)

###
student = {"name": "Alice", "age": 21, "marks": 90}
for values in student.items():
    print(values)'''