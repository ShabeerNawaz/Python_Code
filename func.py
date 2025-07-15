#functions mostly are used 4 reusability of code
#remove the duplicate code
a = 10
b=8

sum = a+b

print(sum)

#more code lines

a=6
b=7

sum=a+b
print(sum)

#function sum

def sum(a,b):
    return a+b

print(sum(4,8))
print(sum(8,9))
print(sum(23,56))

#function will return none when there is no any retun statement
def print_msg():
    print("Hello")

print_msg()

output=print_msg()
print(output)
    
# func 4 avg

def calc_avg(a,b,c):
    avg=(a+b+c)/3
    return avg

print(calc_avg(60,78,90))

list1 =[5,7,9,4,2,1,8,6,4]
list2=["shah", "shani","shabeer","syed","ameer","dilbar"]

#WAF to print length of list

def len_list(lst):
    return(len(lst))

print(len_list(list1))
print(len_list(list2))

#WAF to print elmnt of likst in single line

def print_list(lst):
    for i in lst:
        print(i,end=" ")

print_list(list1)
print()  # for new line
print_list(list2)

#wAF to find factorial of a number

def fact(num):
    if num==1 or num ==0:
        return 1
    else:
        return num*fact(num-1)
    
print(fact(5))

#WAF to convert USD into PKR
def convert_usd_to_pkr(usd):
    pkr = usd *280
    print(usd,"USD = ",pkr,"PKR")

convert_usd_to_pkr(67)

