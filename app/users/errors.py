class UserAlreadyExistsError(Exception):
    code = "USER_ALREADY_EXISTS"

    def __init__(self, field: str):
        self.field = field


class UserNotFoundError(Exception):
    code = "USER_NOT_FOUND"

    def __init__(self, user_id: int):
        self.user_id = user_id
