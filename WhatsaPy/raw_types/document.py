class Document(object):
    caption: str
    filename: str
    sha256: str
    mime_type: str
    id: int

    def __init__(self, document: dict):
        self.caption = document.get('caption', '')
        self.filename = document.get('filename', '')
        self.sha256 = document.get('sha256', '')
        self.mime_type = document.get('mimetype', '')
        self.id = document.get('id', 0)

    def __init__(self, caption: str, filename: str, sha256: str, mime_type: str, id: int):
        self.caption = caption
        self.filename = filename
        self.sha256 = sha256
        self.mime_type = mime_type
        self.id = id