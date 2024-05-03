from src_dev.product_dev import Product

class Smartphone(Product):
    """
    Категория товаров смартфоны
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        """
        Вычисляем общую текущую стоимость в руб. по смартфонам
        """
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        # print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')
        raise TypeError


if __name__ == "__main__":

    product_item = Product('Test', 'Test', 1000, 10)
    product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')


    print(product_item_2.name)
    print(product_item_2.description)
    print(product_item_2.price)
    print(product_item_2.quantity)

    print(product_item_2.efficiency)
    print(product_item_2.model)
    print(product_item_2.memory)
    print(product_item_2.color)

    try:
        product_item + product_item_2
    except TypeError:
        print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')

    print(product_item + product_item == 20000)
    print(product_item_2 + product_item_2 == 40000)