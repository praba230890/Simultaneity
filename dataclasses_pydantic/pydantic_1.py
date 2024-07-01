from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

product = Product(name="Coffee", price=2.99, in_stock=True)

print(product)

product = Product(**{"name":"Coffee", "price":2.00, "in_stock":True})

print(product)

product = Product(**{"name":3, "price":2.00, "in_stock":4})

print(product)