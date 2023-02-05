class Sticker(object):
    mime_type: str
    sha256: str
    id: str
    animated: bool

    def __init__(self, sticker: dict):
        self.mime_type = sticker.get('mimetype', '')
        self.sha256 = sticker.get('sha256', '')
        self.id = sticker.get('id', '')
        self.animated = sticker.get('animated', False)

    def __init__(self, mime_type: str, sha256: str, id: str, animated: bool):
        self.mime_type = mime_type
        self.sha256 = sha256
        self.id = id
        self.animated = animated