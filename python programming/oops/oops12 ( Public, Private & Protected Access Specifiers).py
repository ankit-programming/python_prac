#public - normal variabel jo sab use kersakte hai
#protected(_) - variabel jo use file me use ker sakte hai
#private(__)  - variabel jo hame _ kerke print kerwana padta hai.python es varibal ko name mamling ker deta hai
#Note:- name mammling - script me kuch or dekhe ga lakin print kervate waqt kuch or likhna padega

class PPP:
    pubilc_var = "public"
    _protected_var = "protected"
    __private_var = "private"


print("This is ",PPP.pubilc_var)
print("This is ",PPP._protected_var)#only used in this file
print("This is ",PPP._PPP__private_var )#to print this we have to writte first _classname
