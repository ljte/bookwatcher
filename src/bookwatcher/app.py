from fastapi import FastAPI

from bookwatcher.api import v1_router

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")
app.include_router(v1_router, prefix="/api")