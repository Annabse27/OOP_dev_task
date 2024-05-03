from src_dev.product_dev import Product
from src_dev.smartphone import Smartphone
from src_dev.lawngrass import LawnGrass


def test_print_mixin(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"

    Smartphone('Test_smart2', 'Test_smart2', 2000, 20, 2.5, 'Model2', 20000, 'black')
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Test_smart2', 'Test_smart2', 2000, 20)"

    LawnGrass('Test_grass2', 'Test_grass2', 4000, 40, 'France', '2 years', 'dark green')
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Test_grass2', 'Test_grass2', 4000, 40)"
