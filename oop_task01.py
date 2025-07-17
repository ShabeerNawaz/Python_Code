class Student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"

std1 = Student("shani",24)
std2=Student("Raaj",22)

print(std1)
print(std2)
