#---------------- @classmethod ------------
#agar hame class ke ander ke valeabel ya function ke sath kam kerna hai to ahm class method ka use karenge
class Emp:
    no_of_leave = 5

    def info_printer(self):
        return f"Employee name is {self.name} and salary is {self.sal} and roll is {self.roll}"

    def __init__(self , aname , asal , aroll ):
        self.name = aname 
        self.sal = asal
        self.roll = aroll
    #note:- jas hame pata hai calass me agar ham function banate hai to vo automatically self le leta hai
    #to use avoid kerne ke liye ham @classmethod ka use kerenge or ye class ke instance variabel ko estmal kere ga
    @classmethod
    def change_leave(cls , newleaves):#cls ka matalab ahia class or Emp 
        cls.no_of_leave = newleaves

deepak = Emp("deepak", 400 , "Emp")
deepak.change_leave(10)
print(Emp.no_of_leave)