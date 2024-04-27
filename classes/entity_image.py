# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from uuid import uuid4, UUID

from mongoengine import *

from enums import Status
from .tool_settings import Settings

settings = Settings()
log = logging.getLogger(settings.environment)
connect(
    db=settings.db_name,
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_host
)
"""
    This is a Simple entity that will save an image on base64 encoded form.
"""


class ImageData(Document):
    _uuid = UUIDField(required=True, unique=True, default=uuid4())
    imageData = StringField(required=True, unique=True)
    imageType = StringField()  # This will have the base64encoded data
    imageFilename = StringField(required=True, unique=True)
    imageSize = StringField()
    imageMode = StringField()
    imageFormat = StringField()
    createdAt = DateTimeField(required=True, default=datetime.now())
    status = IntField(required=True, default=Status.REG.value)
    statusDate = DateTimeField(required=True, default=datetime.now())

    def get_data(self):
        return {
            "fileName": f"{self.name}.{self.imageType}",
            "imageSize": self.imageSize,
            "data": self.imageData,
            "mode": self.imageMode,
            "imageType": self.imageType,
            "contentType": f"image/{self.imageType}".lower()
        }

    @staticmethod
    async def get_image_from_uuid(uuid: UUID):
        image = None
        try:
            image = [image for image in ImageData.objects(_uuid=uuid)][-1]
        except ValueError as e:
            log.error(e.__str__())
        finally:
            return image
