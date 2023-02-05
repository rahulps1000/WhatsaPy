class Image(object):
    caption: str
    sha256: str
    id: str
    mime_type: str

    def __init__(self, image: dict):
        self.caption = image.get('caption', '')
        self.sha256 = image.get('sha256', '')
        self.id = image.get('id', '')
        self.mime_type = image.get('mimetype', '')

    def __init__(self, caption: str, sha256: str, id: str, mime_type: str):
        self.caption = caption
        self.sha256 = sha256
        self.id = id
        self.mime_type = mime_type