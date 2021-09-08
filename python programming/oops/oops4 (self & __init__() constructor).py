#------------- constructor -----------

class Emp:
    no_of_leave = 5

    #self:- self vo intance hoga jes per vo function lagaya ja raha hai
    def info_printer(self):
        return f"Employee name is {self.name} and salary is {self.sal} and roll is {self.roll}"
    #yeha self ka matalab object eg:- agar ham info_printer me deepak dalte hai to vo
    #deepak.name deepak.sal ho je ga yane jah aself vaha deepak

    #----------- __init__ -----------
    #it is used to make instance so we have not to writte again and agin down
    def __init__(self , aname , asal , aroll ):
        self.name = aname 
        self.sal = asal
        self.roll = aroll

#__init__ method for making instance from object
kunal = Emp("kunal" , 900 , "programmer")

print(kunal.info_printer())


#old method
'''#-------------- object ----------------
ankit = Emp() 
deepak = Emp()

#--------------- instance variabels--------------  
ankit.name = "ankit"
ankit.sal = 500
ankit.roll = "HR"

deepak.name = "ankit"
deepak.sal = 600
deepak.roll = "employee"'''


#deepak.info_printer me deepak info_printer self ke tor pe arrgumnet hai

#making obejct and giving instance to Emp
