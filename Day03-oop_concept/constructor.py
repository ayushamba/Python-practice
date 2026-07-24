## basic structure of object oriented language 

class factory:
    def __init__(self,material,zip,pockets):
        self.material = material
        self.zip = zip
        self.pockets = pockets
    def show(self ):
        print(f"this is your material: {self.material} ,zip:{self.zip},pockets: {self.pockets}")
rebook = factory("plastic",2,1)
adidas = factory("silicon",4,1)

rebook.show()



