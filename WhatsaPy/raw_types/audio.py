class Audio(object):
    id: int
    mime_type: str

    def __init__(self, audio_data: dict):
        self.id = audio_data.get('id', 0)
        self.mime_type = audio_data.get('mimetype', '')

    def __init__(self, id: int, mime_type: str):
        self.id = id
        self.mime_type = mime_type