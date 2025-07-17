with open("simple.txt","r+") as f:
    f.write(input("Enter text: "))
    data= f.read()
    print(data)