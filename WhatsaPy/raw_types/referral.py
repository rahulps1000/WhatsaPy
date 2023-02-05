class Referral(object):
    source_url: str
    source_type: str
    source_id: str
    headline: str
    body: str
    media_type: str
    image_url: str
    video_url: str
    thumbnail_url: str

    def __init__(self, referral: dict):
        self.source_url = referral.get('sourceUrl', '')
        self.source_type = referral.get('sourceType', '')
        self.source_id = referral.get('sourceId', '')
        self.headline = referral.get('headline', '')
        self.body = referral.get('body', '')
        self.media_type = referral.get('mediaType', '')
        self.image_url = referral.get('imageUrl', '')
        self.video_url = referral.get('videoUrl', '')
        self.thumbnail_url = referral.get('thumbnailUrl', '')

    def __init__(self, source_url: str, source_type: str, source_id: str, headline: str, body: str, media_type: str, image_url: str, video_url: str, thumbnail_url: str):
        self.source_url = source_url
        self.source_type = source_type
        self.source_id = source_id
        self.headline = headline
        self.body = body
        self.media_type = media_type
        self.image_url = image_url
        self.video_url = video_url
        self.thumbnail_url = thumbnail_url