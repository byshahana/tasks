class Student:
    school="ABC School"
    def __init__(self,name):
        self.name=name
    def study(self):
        print(f"{self.name} is studying")
    def __str__(self):
        return self.name
s1= Student("Rahul")
print(s1)
s1.study()

class Student:
    school="ABC School"
def __init__(self,name):
    self.name=name
def study(self):
    print(f"{self.name}is studying")
def __str__(self):
    return self.name
