class ButtonReply(object):
    id: str
    title: str

    def __init__(self, button_reply: dict):
        self.id = button_reply.get('id', '')
        self.title = button_reply.get('title', '')

    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title