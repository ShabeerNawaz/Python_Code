#breake and continue in loop

#continue task
i=0
for i in range(1,10):
    if(i%2==0):
        continue
    else:
        print(i)
    i+=1
#break task
count = 10
while count >= 0:
    if(count==5):
        break
    print(count)
    count-=1