import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "Test_smart1"
    assert smartphone_1.description == "Test_smart1"
    assert smartphone_1.price == 1000
    assert smartphone_1.quantity == 10

    assert smartphone_1.efficiency == 1.5
    assert smartphone_1.model == "Model1"
    assert smartphone_1.memory == 10000
    assert smartphone_1.color == "red"


def test_smartphone_addition(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 50000


def test_smartphone_addition_err(smartphone_1, smartphone_2):
    with pytest.raises(TypeError):
        result = smartphone_1 + 1
        
