class Error(object):
    code: int
    title: str
    message: str
    details: str

    def __init__(self, error: dict):
        self.code = error.get('code', 0)
        self.title = error.get('title', '')
        self.message = error.get('message', '')
        self.details = error.get('error_data', {}).get('details', '')

    def __int__(self, code: int, title: str, message: str, error_data: dict):
        self.code = code
        self.title = title
        self. message = message
        self.details = error_data.get('details', '')

    def __int__(self, code: int, title: str, message: str, details: str):
        self.code = code
        self.title = title
        self. message = message
        self.details = details