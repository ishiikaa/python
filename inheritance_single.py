class Person1:
    def __init__(self, name, age, cocksize):
        self.name = name
        self.age = age
        self.cocksize = cocksize
    def getdata(self):
        print(f"Name is {self.name} and age is {self.age} and cocksize is {self.cocksize}")
class Person2(Person1):
    def getdata(self):
    
        print(f"Name is {self.name} and age is {self.age} and cocksize is {self.cocksize}")
satish_info = Person1("Satish", 18, 6)
ramesh_info = Person2("Ramesh", 19, 6.5)
satish_info.getdata()
ramesh_info.getdata() 
    