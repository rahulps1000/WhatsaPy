class Contact(object):
    wa_id: int
    name: str

    def __init__(self, contact: dict):
        self.wa_id = contact.get('id', 0)
        self.name = contact.get('profile', {}).get('name','')

    def __int__(self, wa_id: int, profile: dict):
        self.wa_id = wa_id
        self.name = profile.get('name','')

    def __init__(self, wa_id: int, name: str):
        self.wa_id = wa_id
        self.name = name