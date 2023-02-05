class ListReply(object):
    id: str
    title: str
    description: str

    def __init__(self, list_reply: dict):
        self.id = list_reply.get('id', '')
        self.title = list_reply.get('title', '')
        self.description = list_reply.get('description', '')

    def __init__(self, id: str, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description