import json
import os

from src_dev.product_dev import Product
from src_dev.category_dev import Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data_dev = json.load(file)
    return data_dev


def created_objects_from_json(data_dev):
    categories = []
    for category in data_dev:
        products = []
        for product in category['products']:
            print(product)
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data_dev = read_json("../data_dev/data_dev.json")
    print(raw_data_dev)
    categories_data = created_objects_from_json(raw_data_dev)

    print(categories_data[0].name)
    print(categories_data[0].products)
