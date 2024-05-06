from src_dev.base_product import BaseProduct
from src_dev.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """
    Класс для учета продуктов по группам
    """
    name: str
    description: str
    price: float
    quantity: int

    # цену нельзя изменять напрямую, устанавливаем префикс private

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.__price = price
        if quantity:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        """
        Возвращаем информацию о товаре в виде
        Наименование товара, 100 руб. Остаток: шт.
        """
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """
        Вычисляем общую текущую стоимость в руб. по всем группам товаров
        """
        if type(other) is Product:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict):
        """
        Задаем  - через Класс создание экземпляра класса: группа товара
        """
        return cls(**product_dict)

    @property
    def price(self):
        """
        метод-геттер для цены с префиксом private
        """
        return self.__price

    @price.setter
    def price(self, price_new):
        """
         метод-сеттер для изменения цены
         """
        if price_new <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = price_new


if __name__ == "__main__":
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1)
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

    var = dict(name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0,
               quantity=1)
    product = Product(**var)
    print(product.name)

    new_product = Product.new_product(product_dict={
        "name": "new_name",
        "description": "new_description",
        "price": 100.0,
        "quantity": 5
    }
    )
    print(new_product.name)

    new_product.price = 150000
    print(new_product.price)

    new_product.price = -20000
    print(new_product.price)

    print(product)
    print(new_product)

    print(product + new_product)

    product_item = Product('Test', 'Test', 1000, 10)
    # product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    # product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')

    product_data = {
        'name': 'New Product',
        'description': 'New Description',
        'price': 500,
        'quantity': 5
    }

    new_product = Product.new_product(product_data)

    try:
        product_user = {
            'name': 'User Product',
            'description': 'User Description',
            'price': 500,
            'quantity': 0
        }
        product_user_zero = Product.new_product(product_user)
    except ValueError as e:
        #print("Товар с нулевым количеством не может быть добавлен")
        print(str(e) == "Товар с нулевым количеством не может быть добавлен")


