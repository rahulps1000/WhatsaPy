class Video(object):
    caption: str
    filename: str
    sha256: str
    id: str
    mime_type: str

    def __init__(self, video: dict):
        self.caption = video.get('caption', '')
        self.filename = video.get('filename', '')
        self.sha256 = video.get('sha256', '')
        self.id = video.get('id', '')
        self.mime_type = video.get('mimetype', '')

    def __init__(self, caption: str, filename: str, sha256: str, id: str, mime_type: str):
        self.caption = caption
        self.filename = filename
        self.sha256 = sha256
        self.id = id
        self.mime_type = mime_type
