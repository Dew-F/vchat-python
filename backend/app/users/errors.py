from app.core.exception.base import AppError


class UserAlreadyExistsError(AppError):
    code = "USER_ALREADY_EXISTS"
    status_code = 409

    def __init__(self, field: str):
        super().__init__(field=field)


class UserNotFoundError(AppError):
    code = "USER_NOT_FOUND"
    status_code = 404

    def __init__(self, user_id: int):
        super().__init__(user_id=user_id)
