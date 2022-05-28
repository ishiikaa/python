class Person1:
    def __init__(self, name, age, cocksize):
        self.name = name
        self.age = age
        self.cocksize = cocksize
    def getdata(self):
        print(f"Name is {self.name} and age is {self.age} and cocksize is {self.cocksize}")
class Person3(Person1):
    def __init__(self, phone_no, wife_name):
        self.phone_no = phone_no
        self.wife_name = wife_name
    def getdata(self):
        print(f"Phone no. is {self.phone_no} and Wife's name is {self.wife_name}")
class Person4(Person1):
    def __init__(self, subject):
        self.subject = subject
    def getdata(self):
        
        print(f"Subject is {self.subject}")
class Person2(Person3, Person4):
    def getdata(self):

        print(f"Name is {self.name} and age is {self.age} and cocksize is {self.cocksize} Phone no. is {self.phone_no} and Wife's name is {self.wife_name} subject is {self.subject} ")
        
#satish_info = Person1("Satish", 18, 6)
#ramesh_info = Person2("Ramesh", 19, 6.5)
Rajesh_info = Person2("Rajesh", 20 , 6.5, 9830986754, "Savita", "python")
#satish_info.getdata()
#ramesh_info.getdata() 
Rajesh_info.getdata()
