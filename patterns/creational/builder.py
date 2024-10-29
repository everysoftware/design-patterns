from patterns.creational.products import Product, ProductShelf


class ProductShelfBuilder:
    """
    Builder is a creational design pattern that lets you construct complex objects step by step.
    The pattern allows you to produce different types and representations of an object using the same construction code.
    """

    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def build(self, category: str) -> ProductShelf:
        self.products.sort()
        return ProductShelf(category, self.products)
