class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        existing_products = file.read()
        file.close()
        return existing_products

    def add(self, *products):
        file = open(self.__file_name, 'a+')
        existing_products = self.get_products()
        for product in products:
            if product.name not in existing_products:
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {Product.__str__(product)} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
