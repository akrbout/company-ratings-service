from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from src.storage import engine, crud
from src.service.profile import ProfileService
from src.api_models import user

app = FastAPI()


@app.on_event("startup")
async def startup():
    await engine.create_db()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.post("/registrate", description="Регистрация пользователя")
async def reg_user(user: user.RegistrateUser) -> user.ProfileStatus:
    create_user = await ProfileService().registrate_user(user)
    if create_user.status is False:
        raise HTTPException(status_code=400, detail=create_user.message)
    else:
        return create_user


@app.get("/healtz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, int]:
    return {"status": status.HTTP_200_OK}
