from io import BytesIO
import logging
from PIL import Image
from inspect import currentframe
from logging import config
from uuid import UUID
import base64
from fastapi.responses import StreamingResponse, FileResponse

from classes import ImageData, Settings
from utils import configure_logging

from tempfile import TemporaryFile

settings = Settings()
log = logging.getLogger(settings.environment)
logging.config.dictConfig(configure_logging())


async def ctr_get_image_data_from_uuid(uuid: UUID) -> ImageData:
    log.info(f"Starting {currentframe().f_code.co_name} uuid: {str(uuid)}")
    image = None
    try:
        image = await ImageData.get_image_from_uuid(uuid=uuid)
    except Exception as e:
        log.error(f"this is an error ---> {e.__str__()}")
    finally:
        log.info(f"{currentframe().f_code.co_name} finish")
        return image


async def ctr_get_image_from_data(data: ImageData):
    img = Image.open(BytesIO(base64.b64decode(data.imageData, validate=True)))
    buf = BytesIO()

    fp = TemporaryFile()
    img.save(fp, data.imageType)
    fp.seek(0)
    return StreamingResponse(
        fp,
        media_type=f"image/{data.imageType}".lower()
    )
