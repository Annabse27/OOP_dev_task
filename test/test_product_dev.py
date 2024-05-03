from src_dev.product_dev import Product

def test_product_init(product_obj):
    assert product_obj.name == "Samsung Galaxy C23 Ultra"
    assert product_obj.description == "256GB, Серый цвет, 200MP камера"
    assert product_obj.price == 180000.0
    assert product_obj.quantity == 5

def test_product_new_created():
    product_new = Product("Name_new", "Description_new", 100000, 100)
    assert product_new.name == "Name_new"
    assert product_new.description == "Description_new"
    assert product_new.price == 100000
    assert product_new.quantity == 100


def test_product_new_update(capsys, product_obj):
    product_obj.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Цена не должна быть нулевая или отрицательная"

    product_obj.price = 150000.0
    assert product_obj.price == 150000.0

def test_product_str(product_obj):
    assert str(product_obj) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_addition_products(product_obj, product_obj_new):
    assert product_obj + product_obj_new == 900500
