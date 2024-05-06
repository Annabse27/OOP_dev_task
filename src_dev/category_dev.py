from src_dev.product_dev import Product
from src_dev.zero_product_add import ZeroProductAdd

class Category:
    """
    Класс категорий для хранения информации по группам товаров
    """
    name: str
    description: str
    products: list

    count_category = 0
    count_product = 0

    # изменить категорию нельзя, применен префикс private

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.count_category += 1
        Category.count_product += len(products) if products else 0

    def __str__(self):
        """
        Выводит текущий остаток (в шт.) товаров по категории

        """
        touts_produits_de_category = sum(list(item.quantity for item in self.product_in_list))
        return f"{self.name}, количество продуктов: {touts_produits_de_category} шт."

    def __add__(self, other):
        """
        Складывает товары (шт/ или руб.) по нужным категоряим
        """
        return self.tout_de_touts() + other.tout_de_touts()

    def tout_de_touts(self):
        """
        метод, который считает внутри КОНКРЕТНОЙ отдельновзятой категории всю стоимость группы продуктов
        """
        if self.product_in_list:
            arr = []
            for item in self.product_in_list:
                # arr.append(item.quantity)
                arr.append(item.quantity*item.price)
            # при условии подсчета внутри категории всего шт ВСЕХ продуктов
            # print(f'Количество продуктов в {self.name} категории: {sum(arr)} шт.')
            # при условии подсчета внутри категории ВСЯ стоимость ВСЕХ продуктов в руб.
            # print(f'Общая стоимость всех продуктов в {self.name} категории: {sum(arr)} руб.')

            return sum(list(arr))
        else:
            # print(f'Количество продуктов в {self.name} категории: 0 шт.')
            # print(f'Общая стоимость всех продуктов в {self.name} категории: 0 руб.')
            return 0


    @property
    def products(self):
        """
        метод-геттер для строкового вывода остатки товара в группе
        """
        product_str = ""
        for item in self.__products:
            product_str += f"{str(item)}\n"
        return product_str

    @products.setter
    def products(self, new_product: Product):
        """
        метод-сеттер для добавления товара (в виде экземпляра класса) в группу
        """
        if isinstance(new_product, Product):
            try:
                if new_product.quantity < 0:
                    raise ZeroProductAdd("Нельзя добавлять несуществующий продукт")
            except ZeroProductAdd as err:
                print(str(err))
            else:
                self.__products.append(new_product)
                Category.count_product += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка завершена")
        else:
            raise TypeError


    @property
    def product_in_list(self):
        """
        метод-геттер для отображения остатка товара в формате list[]
        """
        return self.__products


    def middle_price(self):
        """
        считает средний ценник продукта
        """
        try:
            #return self.tout_de_touts()/sum(list(item.quantity for item in self.product_in_list))
            return (sum(prod.price for prod in self.__products)) / len(self.__products)
        except ZeroDivisionError:
            return 0



if __name__ == "__main__":

    var = dict(name="Телефоны", description="Телефоны в целом")
    category = Category(**var)

    print(category.name)
    print(category.description)
    # это теперь наш сеттер - быть внимательным и отслеживать, как функционирует наш экемпляр_класса.продукт(геттер)
    # print(category.products)


    print(category.count_category)
    print(Category.count_product)

    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    var2 = dict(name="Смартфоны",
                description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                products=[product1, product2, product3])
    category2 = Category(**var2)

    print(category2.count_category)
    # это, чтобы показать, что со всеми категориями и на всех уровнях работает атрибут класса
    # print(Category.count_category)
    # print(category.count_product)

    print(category2.count_product)

    # это мы выводим наш сеттер, чтобы не задавать его тем способом как сверху, а применять к нему действия
    print(category2.products)

    product4 = Product("Name4", "Description4", 500.0, 5)
    product5 = Product("Name5", "Description5", 1500.0, 15)
    product6 = Product("Name6", "Description6", 2500.0, 25)

    category2.products = product4
    category2.products = product5
    category2.products = product6
    print(category2.products)

    print(len(category2.product_in_list))

    print(category)
    print(category2)

    print()

    print(category2.middle_price())
    print(category.middle_price())

    #Проверки к последней devoirs

    product7 = Product('1','1', 10, -5)
    category2.products = product7

    category_null = Category('Test', 'Test', [])
    print(category_null.middle_price() == 0)




