import pydantic
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from src.storage import engine, crud
from src.service.profile import ProfileService
from src.api_models import user
from src import errors


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=create_user.message)
    else:
        return create_user


@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        auth_model = user.AuthUser(username=form_data.username, password=form_data.password)
    except pydantic.ValidationError as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bad data validation: {ex}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        auth_session = await ProfileService().authenticate_user(auth_model)
        return {"access_token": auth_session.access_token, "token_type": "bearer"}
    except errors.BadPassword:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.get("/healtz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, int]:
    return {"status": status.HTTP_200_OK}
