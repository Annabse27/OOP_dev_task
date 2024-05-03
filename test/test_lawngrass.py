import pytest


def test_lawngrass_init(lawngrass_1):
    assert lawngrass_1.name == 'Test_grass1'
    assert lawngrass_1.description == 'Test_grass1'
    assert lawngrass_1.price == 3000
    assert lawngrass_1.quantity == 30

    assert lawngrass_1.country == 'Canada'
    assert lawngrass_1.germination_period == '1 year'
    assert lawngrass_1.color == 'light green'


def test_lawngrass_addition(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 250000


def test_lawngrass_addition_err(lawngrass_1, lawngrass_2):
    with pytest.raises(TypeError):
        result = lawngrass_1 + 1
