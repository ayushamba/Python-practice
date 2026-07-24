class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls,text):
        name , price = text.split("-")
        return cls(name,price)

p1 = Product.from_string("Laptop-65000")

print(p1.name)
print(p1.price)