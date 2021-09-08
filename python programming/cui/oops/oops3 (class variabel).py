#--------------------- class varibel ----------------------
#varibels present in class
#that value or variabel will same for all class objects
 
class Emp:
    no_of_leave = 5

#-------------- object ----------------
ankit = Emp() 
deepak = Emp()

#--------------- instance variabels--------------  
ankit.name = "ankit"
ankit.sal = 500
ankit.roll = "HR"

deepak.name = "ankit"
deepak.sal = 600
deepak.roll = "employee"

print("printing no_of_leave from ankit class boject = " , ankit.no_of_leave)
print("printing no_of_leave from deepak class boject =" , deepak.no_of_leave)
print("printing no_of_leave from class Emp = " , Emp.no_of_leave , "\n")

#if you want to change  no_of_leave 
Emp.no_of_leave = 8
print("changed Emp no_of_leave from Emp = ", Emp.no_of_leave , "\n")

#------------__dict__------------
#it is attribut which return class obecjt dictionary\n
print("deepak info befroe trying to change leave from deepak class object = " , deepak.__dict__)
#Note:- you cant change class variabel through class object
#eg
deepak.no_of_leave = 8
print("deepak info after trying to change leave from deepak class object = " , deepak.__dict__)