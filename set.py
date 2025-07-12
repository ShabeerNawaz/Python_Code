#practice tasks
collection={4,7,"shah",3,2,1,"shani",5,6,"syed"}

print(collection)

#sets methods
col_1=set()

col_1.add(4)
col_1.add(9)
col_1.add(6)
col_1.add((43,67,3))

#col_1.add([6,8,5,4]) # This line would raise an error because lists are not hashable and cannot be added to a set.

print(col_1)

col_1.add("shabeer")
col_1.remove(9)

print(col_1)

col_2={7,17,2,1,8,4,21}

print(col_2.pop())
print(col_2.pop())
print(col_2.pop())

