class ReferredProduct(object):
    catalog_id : str
    product_retailer_id : str

    def __init__(self, referred_product: dict):
        self.catalog_id = referred_product.get('catalogId', '')
        self.product_retailer_id = referred_product.get('productRetailerId', '')

    def __init__(self, catalog_id: str, product_retailer_id: str):
        self.catalog_id = catalog_id
        self.product_retailer_id = product_retailer_id