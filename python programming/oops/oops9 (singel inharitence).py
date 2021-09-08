#----------------- Inharintanc -----------------
#es me ham phale se bane hue class ko use karenge doosre class me
#ab ham phele walle class ko doosre class me copy past be jer salte hai laken agar ham asa kerte hai to 
#code reusabel nahi rhe jaye ga

#making first class
class Class1:
    def __init__(self, pname, page):
        self.name = pname
        self.age = page
    
    @classmethod
    def str_obj(cls, string):
        return cls(*string.split("-"))

    
    def print_class1(self):
        return f"name is {self.name} and age is {self.age}"

ankit = Class1.str_obj("ankit-18")
deepak = Class1.str_obj("deepak-20")
print(ankit.name,deepak.name)


#creating second class
class Class2(Class1):
    #mane es class me kuch nahi banaya hai bass mane class ke ander class rakhe or phele walle class ke
    #sare function , attribute or class variabl be agaye 
    #2>.es me ham es function ke khud ka be constructor bana sakte hai
    #for eg making constructor
    def __init__(self, pname, page, psec):
        self.name = pname
        self.age = page
        self.sec = psec
        #ye constructor class1 walle constructor se milta julta hai 
        #es constructor ko ham bina copy paste kere be modify ker sakte the """"SUPER""""" ke madad se kyoke 
        #ham class2 ke ander class1 usee ker rahe hai. vo hamm doosr file me smjange

    #now making a function
    def print_class2(self):
        return f"name is {self.name} and age is {self.age}"
        #jo function hame banaya hai vasa function classs1 me be tha jese modifiy ker

kunal = Class2.str_obj("kunal-19")
print(deepak.print_class1())