#for loop tasks:

"""
list=[5,3,2,5,6,9,8,2]

for i in list:
    print(i) 
    
str1 ="Hello World"
for char in str1:
    print(char)
     
list_str=["shabeer", "shah" ,"shanu", "shabaz"]
for key in list_str:
    print(key)
else:
    print("End of program")    

#simple print the numbers in a list
list = [1,4,9,16,25,36,49,64,81,100,49]

for item in list:
    print(item)

#finding an element in list
list = [1,4,9,16,25,36,49,64,81,100,49]

x = int(input("Enter x number for searching in a list: "))
for item in list:
    if x==item:
        print(x," is Found...")
        break
else:
    print(x," is not found...")
"""

numbers=range(1,5)

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

num=range(10) # stop at 10

for i in num:
    print(i)
    
num1=range(1,5) # start and stop conditions

for item in num1:
    print(item)
    
num2=range(1,10,2) #start ,stop and step conditions
#Odd numbers from 1 to 10
for item in num2:
    print(item)
    
    