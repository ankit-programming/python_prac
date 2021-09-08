#Abstraction :- es ka matlab hota hai kese kam ko tukdo me tod dena
#Encapsulation :- es ka matlab hota hai detalis ko hed kerna
#yane hame bas class ke function ko chalane se matlab hai bas nake us ko samanj ne me

#abrteact base class
#ab ager ap programmer ko force kerna chate ho ke Comon me bana hua function har class me dubara mnbanana hai
#to ham @abstracmethod ka use kerte hai
from abc import ABC , abstractmethod
#ye import line @abstraction ko use kenre ke liye hai
#agar hame kese class ka function doosre class me kerna hai to ham @abstractmethod ka use kerenge
class Comon(ABC):
    @abstractmethod
    def fun(self):
        return "this is comon class"


class A(Comon):
    def __init__(self ,abc):
        self.abc = abc

    def __str__(self):
        return f"{self.abc}"

b = A("ankit")

print(a)

#not understand much