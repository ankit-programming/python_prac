#---------------- staic method --------------
#agar apko function banate waqt na instance variabel chaye na class ka variabel chaye to ham 
# @staicmethos ko use karenge
# or agar app chate hai ko vo function sirf apke class obejct pe run 
class Emp:
    no_of_leave = 5

    def info_printer(self):
        return f"Employee name is {self.name} and salary is {self.sal} and roll is {self.roll}"

    def __init__(self , aname , asal , aroll ):
        self.name = aname 
        self.sal = asal
        self.roll = aroll

    @classmethod
    def inst_str(cls , string):
        #param = string.split("-")
        #return cls(param[0] , param[1] , param[2])
        #in one line
        return cls(*string.split("-"))# * ka matlab hai args


shubham = Emp.inst_str("shubham-100-HR")







