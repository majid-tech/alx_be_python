# Creating objects ...

# class tutor:
#     def __init__(self, name, age, level):
#         self.name = name
#         self.age = age
#         self.level = level

#     def tutor_info(self):
#         return f'Tutor name: {self.name} | Tutor age: {self.age} | Tutor level: {self.level}'
    
# tutor1 = tutor('Majid', 30, 400)

# print(tutor1.tutor_info())

# product catalog

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return f'product: {self.name} | price: {self.price} | quantity: {self.quantity} = {self.price * self.quantity}'

p1 = Product("jilbab", 350, 12)
print(p1.calculate_total())