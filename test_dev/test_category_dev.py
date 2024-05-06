import pytest
from src_dev.product_dev import Product


def test_category1_init(category1):
    assert category1.name == "Телефоны"
    assert category1.description == "Телефоны в целом"


def test_category2_init(category2):
    assert category2.name == "Смартфоны"
    assert category2.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"

    assert len(category2.product_in_list) == 3
    assert category2.count_category == 2
    assert category2.count_product == 3


def test_category_property(category2):
    assert category2.products == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                  'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test_category_setter(category2, product_obj):
    assert len(category2.product_in_list) == 3
    category2.products = product_obj
    assert len(category2.product_in_list) == 4

    assert category2.products == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                  'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
                                  'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n')


def test_category_str(category2):
    assert str(category2) == "Смартфоны, количество продуктов: 27 шт."


def test_category_setter_err(category2, product_obj):
    with pytest.raises(TypeError):
        category2.products = 1


def test_category_setter_smartphone(category2, smartphone_1):
    assert 3 == len(category2.product_in_list)
    category2.products = smartphone_1
    assert 4 == len(category2.product_in_list)


def test_middle_price(category2, category1):
    assert category1.middle_price() == 0
    assert category2.middle_price() == 140333.33333333334


def test_user_exeption(capsys, category2):
    assert len(category2.product_in_list) == 3

    product_user_zero = Product('test_zero', 'test_zero', 10, -2)
    category2.products = product_user_zero
    message = capsys.readouterr()

    assert message.out.strip().split('\n')[-2] == "Нельзя добавлять несуществующий продукт"
    assert message.out.strip().split('\n')[-1] == "Обработка завершена"

    product_user_zero = Product('test_zero', 'test_zero', 10, 2)
    category2.products = product_user_zero
    message = capsys.readouterr()

    assert message.out.strip().split('\n')[-2] == "Продукт добавлен успешно"
    assert message.out.strip().split('\n')[-1] == "Обработка завершена"
    