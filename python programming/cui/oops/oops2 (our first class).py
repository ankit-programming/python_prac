#Creating our first class
class Emp: #Emp is class name. Note:-do not use () , class name first letter will capital
    pass

#-------------- object ----------------
#object ye hamm ese ek dibbe ke thrahe man lete hai jes me ham kuch na kuch saman dalenge 
ankit = Emp() # () lagana jarure hai nahi to vo variabel mana jaye ga
deepak = Emp()

#ankit and deeoak are two deffrebt thing of same class 
print("proof = |" , ankit , " || " ,  deepak , "|")

#--------------- instance variabels--------------
#dibbe me bhare jane walla sman yane obejct ke ander fill hone walle detals instance hoti hai
ankit.name = "ankit"
ankit.sal = 500
ankit.roll = "HR"

deepak.name = "ankit"
deepak.sal = 600
deepak.roll = "employee"
#Note:- you can use list , dict , tupleetc also


#------------------ printing instance info -------------------- 
print(ankit.name)
