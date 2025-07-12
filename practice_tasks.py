#WAP to find sum of n numbers: using while loop

n=int(input("Enter a number:"))
sum=0
while n>0:
    sum+=n
    n-=1
print("sum of n numbersis : ",sum)

#WAP to find the factorial of first n number : using for

num=int(input("Enter the number: "))

fact=1
for i in range(1,num+1):
    fact*=i
print("factorial of num is: ", fact)