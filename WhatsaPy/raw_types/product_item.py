class ProductItem(object):
    product_retailer_id: str
    quantity: str
    item_price: str
    currency: str

    def __init__(self, product_item: dict):
        self.product_retailer_id = product_item.get('product_retailer_id', '')
        self.quantity = product_item.get('quantity', '')
        self.item_price = product_item.get('item_price', '')
        self.currency = product_item.get('currency', '')

    def __init__(self, product_retailer_id: str, quantity: str, item_price: str, currency: str):
        self.product_retailer_id = product_retailer_id
        self.quantity = quantity
        self.item_price = item_price
        self.currency = currency