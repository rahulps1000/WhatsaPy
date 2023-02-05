from WhatsaPy.raw_types.referred_product import ReferredProduct
class Context(object):
    forwarded : bool
    frequently_forwarded : bool
    from_id : str
    id : str
    referred_product : ReferredProduct

    def __init__(self, context: dict):
        self.forwarded = context.get('forwarded', False)
        self.frequently_forwarded = context.get('frequently_forwarded', False)
        self.from_id = context.get('from', '')
        self.id = context.get('id', '')
        self.referred_product = ReferredProduct(context.get('referred_product', {}))

    def __init__(self, forwarded: bool, frequently_forwarded: bool, from_id: str, id: str, referred_product: ReferredProduct):
        self.forwarded = forwarded
        self.frequently_forwarded = frequently_forwarded
        self.from_id = from_id
        self.id = id
        self.referred_product = referred_product