from typing import Union
from WhatsaPy.raw_types.button_reply import ButtonReply
from WhatsaPy.raw_types.list_reply import ListReply
class Interactive(object):
    type: Union[ButtonReply, ListReply]

    def __init__(self, interactive: dict):
        self.type = ListReply(interactive.get('type', {})) if 'description' in interactive.get('type', {}) else ButtonReply(interactive.get('type', {}))

    def __init__(self, type: Union[ButtonReply, ListReply]):
        self.type = type