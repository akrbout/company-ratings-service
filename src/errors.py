class UnknowedUserError(BaseException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class UserOrEmailExistError(BaseException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
