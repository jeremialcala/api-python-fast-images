import json
import logging.config
import time
from uuid import UUID, uuid4

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi import status
from classes import Settings
from utils import configure_logging
from controllers import ctr_stream_image_from_data, ctr_get_image_data_from_uuid, ctr_get_image_data_from_filename
from constants import CONTENT_TYPE, CONTENT_LENGTH, PROCESSING_TIME, APPLICATION_JSON

description = """
This is QRCode Generator, this component Generates QrCodes from some data send in request.

## Image 

* /image: this endpoint .

* 

"""

tags_metadata = [
    {
        "name": "show",
        "description": "In this operation using some simple data, "
                       "you will create a new Qr Code, ",
    }
]

settings = Settings()
log = logging.getLogger(settings.environment)

app = FastAPI(
    openapi_tags=tags_metadata,
    on_startup=[configure_logging],
    title="Image renderer",
    description=description,
    summary="Simple API that returns images",
    version="0.0.1",
    terms_of_service="https://web-ones.com",
    contact={
      "name": "Jeremi Alcala",
      "url": "https://web-ones.com",
      "email": "jeremialcala@gmail.com",
    },
    license_info={
      "name": "Apache 2.0",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.middleware("http")
async def interceptor(request: Request, call_next):
    log.info(f"new request from: {request.client}")
    start_time = time.time()

    response = Response(
        content=json.dumps({"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "msg": "INTERNAL SERVER ERROR"}),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        headers={CONTENT_TYPE: APPLICATION_JSON}
    )
    try:
        log.info(request.url.path)
        [log.debug(f"Header! -> {hdr}: {val}") for hdr, val in request.headers.items()]
        response = await call_next(request)
    except HTTPException as e:
        response = Response(status_code=e.status_code)
    except Exception as e:
        log.error(e.args)
    finally:
        process_time = "{:f}".format(time.time() - start_time)
        response.headers[PROCESSING_TIME] = str(process_time)
        log.info(f"This request was processed on {process_time} seconds")
        return response


@app.get("/image/{uuid}")
async def get_image_from_uuid(uuid: str):
    return await ctr_stream_image_from_data(await ctr_get_image_data_from_uuid(uuid=UUID(uuid)))


@app.get("/image")
async def get_image_from_filename(filename: str):
    return await ctr_stream_image_from_data(await ctr_get_image_data_from_filename(filename=filename))
