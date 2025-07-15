#print n to 1 backwords

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(3)

#factorial

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))

#sum of first n natural numbers

def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
    
print(sum(5))

#recursive function for print the all element in a list
def list_el(ls,index):
    if(len(ls) == index):
        return
    else:
        print(ls[index])
        return list_el(ls,index+1)
lst = ["champa","chinkni","chambeli","chinki"]
idx=0
list_el(lst,idx)