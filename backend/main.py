import uvicorn
from core.config import settings
from fastapi import FastAPI

app = FastAPI(**settings.app.model_dump(exclude={"host", "port"}))


@app.get("/")
async def root():
    return {"success": True, "msg": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.app.host, port=settings.app.port)
