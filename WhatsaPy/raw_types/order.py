from typing import List

from WhatsaPy.raw_types.product_item import ProductItem


class Order(object):
    catalog_id: str
    text: str
    product_items: List[ProductItem]

    def __init__(self, order: dict):
        self.catalog_id = order.get('catalog_id', '')
        self.text = order.get('text', '')
        self.product_items = [ProductItem(product_item) for product_item in order.get('product_items', [])]

    def __init__(self, catalog_id: str, text: str, product_items: List[ProductItem]):
        self.catalog_id = catalog_id
        self.text = text
        self.product_items = product_items