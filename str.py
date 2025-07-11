str = "shabeer"
str1='shani'
str2="""shah"""

print(str + str1 + str2)
print(str[2:5])
print(str2[-4:-1])
print(str.endswith("er"))
print(str1.capitalize())
print(str2.replace("a","aa"))

#Condition Statements

#first program to check traffic light color
light = input("Enter traffic light color:")
if(light=="red"):
    print("Stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("wait")
else:
    print("Invalid Input")
print("End of Program")

#grade calculation program

marks=int(input("Enter your Marks"))

if(marks<=100 and marks>0):
    if(makes >=90):
        print("Grade A")
    elif(marks>=80 and marks<90):
        print("Grade B")
    elif(marks>=70 and marks<80):
        print("Grade C")
    elif(marks >=60 and marks<70):
        print("Grade D")
    elif(marks >=50 and marks <60):
        print("Pass *")
    else:
        print("Fail")