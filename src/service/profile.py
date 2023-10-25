from src.storage import crud, models as db_models
from src.api_models.user import User as ApiUser, RegistrateUser, ProfileStatus
from src import errors


class ProfileService:
    def __init__(self):
        self.db = crud.StorageSession()

    async def registrate_user(self, reg_data: RegistrateUser) -> ProfileStatus:
        try:
            user_db = db_models.User(
                username=reg_data.username,
                email=reg_data.email,
                key=reg_data.password,
                role=reg_data.role.value,
            )
            result, status_message = await self.db.create_user(user_db)
            return ProfileStatus(status=result, message=status_message)
        except errors.UserOrEmailExistError as ex:
            return ProfileStatus(status=False, message=ex.message)
