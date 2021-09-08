#using classmethod to give inpute make instance in one line
class Emp:
    no_of_leave = 5

    @property #this use when you want function to be use without using()  at last Note:- now this will take no input
    #if you want to give input to info_printer then use setter mehtod
    def info_printer(self):
        return f"Employee name is {self.name} and salary is {self.sal} and roll is {self.roll}"
    
    #demo of setter
    @info_printer.setter
    def info_printer(self , xyz):
        #jo be work hoga vo yeaha lekha jayega
        ...
    
    def __init__(self , aname , asal , aroll ):
        self.name = aname 
        self.sal = asal
        self.roll = aroll

    @classmethod
    def change_leave(cls , newleaves):
        cls.no_of_leave = newleaves

    @classmethod
    def inst_str(cls , string):
        #param = string.split("-")
        #return cls(param[0] , param[1] , param[2])
        #in one line
        return cls(*string.split("-"))# * ka matlab hai args



shubham = Emp.inst_str("shubham-100-HR")
ankit = Emp.inst_str("ankit-500-student")
print(ankit.info_printer)#benifit of @property
print(ankit.info_printer())#if @property was not use then we have to writte this , this statmnet will give error
#becuse we have used @property up side
         

