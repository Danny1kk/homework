class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            content = file.read().strip()
            file.close()
            return content
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products().split('\n') if self.get_products() else []

        products_dict = {}

        for line in existing_products:
            if line.strip():
                parts = line.split(', ')
                name = parts[0]
                weight = float(parts[1])
                category = parts[2]
                products_dict[(name, category)] = weight

        file = open(self.__file_name, 'w')

        for product in products:
            key = (product.name, product.category)
            if key in products_dict:
                products_dict[key] += product.weight
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {products_dict[key]}')
            else:
                products_dict[key] = product.weight

        for (name, category), weight in products_dict.items():
            file.write(f'{name}, {weight}, {category}\n')

        file.close()

# Пример выполняемого кода:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())