#------------------ Multipal inharentance --------------
#ek class me 2 ya 2 se jada class rakhna multipal inharrntance ho ga jasse me class1 class2 ko class3 rekh doo

#class1
class Class1:
    var = 1
    def __init__(self, pname, page):
        self.name = pname
        self.age = page
    
    @classmethod
    def str_obj(cls, string):
        return cls(*string.split("-"))

    
    def print_class1(self):
        return f"name is {self.name} and age is {self.age}"


#creating second class
class Class2:
    var = 2
    def __init__(self, pname, page, psec):
        self.name = pname
        self.age = page
        self.sec = psec
    def print_class2(self):
        return f"name is {self.name} and age is {self.age}.Section is {self.sec}"
    

ankit = Class1.str_obj("ankit-18")
deepak = Class2("deepak", 5,"A")

#multipal inharetance
class Class3(Class1 ,Class2):
    pass

#Notes
#1>.ager hamm class3 ka init constructor , variabel, function  nahi banaynge to vo class1 ke init constructor ko use kerega kyoke 
#class3 me hamn phale class1 lihka hai eg
#2>.
kunal = Class3("kunal", "10")
print(kunal.print_class1())#yha pe ham class2 ka be function use ker sakte the

print("proof that if ther is no function or variabel it use class1 variable or function",kunal.var)