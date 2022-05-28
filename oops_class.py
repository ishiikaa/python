# create a class programmer for storing information of few 
#programmers working at microsoft

class Programmer():
    company = "Microsoft"
    
    def __init__(self,name, product):
        self.name = name
        self.product = product
        
    def getInfo(self):
        print(f"Name: {self.name} \nProduct: {self.product}")
ishika = Programmer("ishika", "nykaa")
sheela = Programmer("sheela", "Lakme")
ishika.getInfo()
sheela.getInfo()
        
