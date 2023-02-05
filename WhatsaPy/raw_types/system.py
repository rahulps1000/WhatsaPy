class System(object):
    body: str
    identity: str
    new_wa_id: str
    wa_id: str
    type: str
    customer: str

    def __init__(self, system: dict):
        self.body = system.get('body', '')
        self.identity = system.get('identity', '')
        self.new_wa_id = system.get('new_jid', '')
        self.wa_id = system.get('jid', '')
        self.type = system.get('type', '')
        self.customer = system.get('customer', '')

    def __init__(self, body: str, identity: str, new_wa_id: str, wa_id: str, type: str, customer: str):
        self.body = body
        self.identity = identity
        self.new_wa_id = new_wa_id
        self.wa_id = wa_id
        self.type = type
        self.customer = customer