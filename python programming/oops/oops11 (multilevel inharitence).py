#---------------- miltiplevel inherntace --------
#this is mostly avoided by programmer beacuse it make confuse

class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

#phele class ke ander dusre class or phir tesre ke ander doosre
#Note:-grandon walle class me vo phele son me variabel ya function ko dekhe ga agar nahi mila to son dad walle class me jayega
