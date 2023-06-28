from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mangum import Mangum

from config.setting import APP_ENV, PROJECT_NAME, LANGUAGE, WEB_URL
from config.database import db

# from core.api import api_router
# import i18n
import os
import time

# Load translation

# i18n.load_path.append(os.path.dirname(os.path.realpath(__file__)) + "/langs")
# i18n.set("locale", LANGUAGE)
# i18n.set("file_format", "yml")

docs_url = "/docs" if APP_ENV == "dev" else None
redoc_url = "/redoc" if APP_ENV == "dev" else None
openapi_url = "/openapi.json" if APP_ENV == "dev" else None

app = FastAPI(
    title=f"{PROJECT_NAME} api",
    docs_url=docs_url,
    redoc_url=redoc_url,
    openapi_url=openapi_url,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[WEB_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check connections with db
@app.on_event("startup")
async def startup():
    if db.is_closed():
        db.connect()


@app.on_event("shutdown")
async def shutdown():
    if not db.is_closed():
        db.close()


# app.include_router(api_router)


# handler = Mangum(app)
def handler(event, context):
    # early return call when the function is called by warmup plugin
    if event.get("source") == "serverless-plugin-warmup":
        # delay 1 secs to prevent reuse the previous invocations container
        time.sleep(1)
        # print("WarmUp - Lambda is warm!")
        return {}

    asgi_handler = Mangum(app)
    # Call the instance with the event arguments
    response = asgi_handler(event, context)

    return response

app = FastAPI()

@app.get('/')
def test():
    return {'msg': 'cln'}