f = open("simple.txt","r")
#read all data inside the file
data = f.read()
print(data)

#read data line by line
line1 = f.readline()
print(line1)

#check the type of data
print(type(line1))

f.close()