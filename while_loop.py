#while loop tasks:
count=1
while count <= 5 :
     #print("hello")
     count=count+1

#printing 1 to 10 using while loop
i=1
while i <= 10:
    #if i==5:
        #break
    #print(i)
    i+=1
#100 to 1 using while loop
num=100
while num >= 1:
    if num %2 == 0:
        #continue  #skip even numbers
        print("even number: ", num)
    else:
        print("Odd number: ",num)
    num-=1
#using while loop and printing tables
num1=1
while num1<=10:
    print(num1," x 4 = ",num1*4)
    num1+=1
    
num2=1
while num2 <= 10:
    if(num2%2 == 0):
        continue #skip even numbers
    else:
        print(num2)
    num2+=1
    
    