from fastapi import FastAPI, status
from src.settings import service_settings
from src.storage import engine, crud

app = FastAPI()


@app.on_event("startup")
async def startup():
    await engine.create_db()


@app.get("/")
async def root():
    db = crud.StorageSession()
    user = await db.is_user_exist("test")
    return user


@app.get("/healtz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, int]:
    return {"status": status.HTTP_200_OK}
