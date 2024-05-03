import pytest

from src_dev.category_dev import Category
from src_dev.product_dev import Product
from src_dev.smartphone import Smartphone
from src_dev.lawngrass import LawnGrass


@pytest.fixture
def product_obj():
    return Product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )

@pytest.fixture
def product_obj_new():
    return Product(
        "prodct_new",
        "description_new",
        100.0,
        5
    )


@pytest.fixture
def category1():
    return Category(
        name="Телефоны",
        description="Телефоны в целом",
        products=[]
    )


@pytest.fixture
def category2():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
                    "удобства жизни",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ]
    )

@pytest.fixture
def smartphone_1():
    return Smartphone('Test_smart1', 'Test_smart1', 1000, 10, 1.5, 'Model1', 10000, 'red')

@pytest.fixture
def smartphone_2():
    return Smartphone('Test_smart2', 'Test_smart2', 2000, 20, 2.5, 'Model2', 20000, 'black')

@pytest.fixture
def lawngrass_1():
    return LawnGrass('Test_grass1', 'Test_grass1', 3000, 30, 'Canada', '1 year', 'light green')

@pytest.fixture
def lawngrass_2():
    return LawnGrass('Test_grass2', 'Test_grass2', 4000, 40, 'France', '2 years', 'dark green')