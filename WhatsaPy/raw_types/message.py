from typing import List

from WhatsaPy.raw_types.audio import Audio
from WhatsaPy.raw_types.button import Button
from WhatsaPy.raw_types.context import Context
from WhatsaPy.raw_types.document import Document
from WhatsaPy.raw_types.error import Error
from WhatsaPy.raw_types.image import Image
from WhatsaPy.raw_types.interactive import Interactive
from WhatsaPy.raw_types.order import Order
from WhatsaPy.raw_types.referral import Referral
from WhatsaPy.raw_types.sticker import Sticker
from WhatsaPy.raw_types.system import System
from WhatsaPy.raw_types.text import Text
from WhatsaPy.raw_types.video import Video


class Message(object):
    audio: Audio
    button: Button
    context: Context
    document: Document
    errors: List[Error]
    from_user: str
    id: str
    image: Image
    interactive: Interactive
    order: Order
    referral: Referral
    sticker: Sticker
    system: System
    text: Text
    timestamp: str
    type: str
    video: Video

    def __init__(self, message: dict):
        self.audio = Audio(message.get('audio', {}))
        self.button = Button(message.get('button', {}))
        self.context = Context(message.get('context', {}))
        self.document = Document(message.get('document', {}))
        self.errors = [Error(error) for error in message.get('errors', [])]
        self.from_user = message.get('from', '')
        self.id = message.get('id', '')
        self.image = Image(message.get('image', {}))
        self.interactive = Interactive(message.get('interactive', {}))
        self.order = Order(message.get('order', {}))
        self.referral = Referral(message.get('referral', {}))
        self.sticker = Sticker(message.get('sticker', {}))
        self.system = System(message.get('system', {}))
        self.text = Text(message.get('text', {}))
        self.timestamp = message.get('timestamp', '')
        self.type = message.get('type', '')
        self.video = Video(message.get('video', {}))

    def __init__(self, audio: Audio, button: Button, context: Context, document: Document, errors: List[Error], from_user: str, id: str, image: Image, interactive: Interactive, order: Order, referral: Referral, sticker: Sticker, system: System, text: Text, timestamp: str, type: str, video: Video):
        self.audio = audio
        self.button = button
        self.context = context
        self.document = document
        self.errors = errors
        self.from_user = from_user
        self.id = id
        self.image = image
        self.interactive = interactive
        self.order = order
        self.referral = referral
        self.sticker = sticker
        self.system = system
        self.text = text
        self.timestamp = timestamp
        self.type = type
        self.video = video