from fastapi import FastAPI, status
from src.router import auth
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer

from src.storage import engine

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="Company Ratins Service",
    description="Сервис для работы с отзывами, собранными с различных площадок",
    version="0.1.0",
)


@app.on_event("startup")
async def startup():
    await engine.create_db()


# SERVICE AUTH ROUTERS
app.include_router(auth.router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/healtz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, int]:
    return {"status": status.HTTP_200_OK}
