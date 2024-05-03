from src_dev.product_dev import Product

class LawnGrass(Product):
    """
    Категория товаров трава газонная
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        """
        Вычисляем общую текущую стоимость в руб. по траве газонной
        """
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        # print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')
        raise TypeError


if __name__ == "__main__":
    product_item = Product('Test', 'Test', 1000, 10)
    product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')

    try:
        product_item + product_item_3
    except TypeError:
        print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')

    print(product_item_3 + product_item_3 == 60000)