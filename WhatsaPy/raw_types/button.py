class Button(object):
    payload: str
    text: str

    def __init__(self, button: dict):
        self.payload = button.get('payload', '')
        self.text = button.get('text', '')

    def __init__(self, payload: str, text: str):
        self.payload = payload
        self.text = text