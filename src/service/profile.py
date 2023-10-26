from src.storage import crud, models as db_models
from datetime import datetime, timedelta
from src.api_models.user import User as ApiUser, RegistrateUser, ProfileStatus, AuthUser, AuthStatus, AccountRoles
from src.settings import auth_settings
from jose import JWTError, jwt
from passlib.context import CryptContext
from src import errors


class ProfileService:
    def __init__(self):
        self.db = crud.StorageSession()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self._auth_settings = auth_settings

    def _create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._auth_settings.secret, algorithm=self._auth_settings.algorithm)
        return encoded_jwt

    async def authenticate_user(self, auth_data: AuthUser) -> AuthStatus:
        db_user: db_models.User = self.db.get_user_by_username(auth_data.username)
        if not db_user:
            return AuthStatus(status=False, user=None)
        is_password_correct = self.pwd_context.verify(auth_data.password, db_user.key)
        if not is_password_correct:
            raise errors.BadPassword(message="Bad password")
        user = ApiUser(
            username=db_user.username,
            email=db_user.email,
            role=AccountRoles(db_user.role),
            full_nm=db_user.full_nm,
        )
        data = dict(user=user.model_dump())

    async def registrate_user(self, reg_data: RegistrateUser) -> ProfileStatus:
        try:
            hashed_password = self.pwd_context.hash(reg_data.password)
            user_db = db_models.User(
                username=reg_data.username,
                email=reg_data.email,
                key=hashed_password,
                role=reg_data.role.value,
            )
            result, status_message = await self.db.create_user(user_db)
            return ProfileStatus(status=result, message=status_message)
        except errors.UserOrEmailExistError as ex:
            return ProfileStatus(status=False, message=ex.message)
