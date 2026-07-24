## data = Ayush-21-India 

class info:

    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    @classmethod
    def from_string(cls,text):
        name,age,place = text.split("-")
        return cls(name,age,place)

i1 = info.from_string("Ayush-21-India")

print(i1.name)
print(i1.age)
print(i1.place)