

class WhatsApp(object):
    """WhatsApp Client

    Parameters:-
        token (``str``):
            Token for the WhatsApp cloud API from developer portal.
        phone_number_id (``int`` | ``str``):
            Phone number id for the WhatsApp cloud API from developer portal.
        verify_token (``str``, *optional*):
            Verify token for verifying the webhook.
    """

    def __int__(self, token=None, phone_number_id=None, verify_token=None):
        self.token = token
        self.phone_number_id = phone_number_id
        self.api_version = "v16.0"
        self.base_url = f"https://graph.facebook.com/{self.api_version}"
        self.url = f"{self.base_url}/{phone_number_id}/messages"

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        if verify_token:
            from flask import Flask
            self.app = Flask(__name__)
            self.app.verify_token = verify_token

    def run(self, *args, **kwargs):
        """Run webhook as localhost for incoming updates"""
        self.app.run(*args, **kwargs)