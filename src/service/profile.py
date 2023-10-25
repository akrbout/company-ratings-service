from src.storage import crud, models


class ProfileService:
    def __init__(self):
        self.db = crud.StorageSession()

    async def registrate_user(self):
        pass
