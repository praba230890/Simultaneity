from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

product = Product("Coffee", 2.99, True)
print(product)

print(Product(2, 3, 4))