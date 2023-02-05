class Text(object):
    body: str

    def __init__(self, text: dict):
        self.body = text.get('body', '')

    def __init__(self, body: str):
        self.body = body