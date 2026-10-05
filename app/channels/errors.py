from app.core.exception.base import AppError


class ChannelAlreadyExistsError(AppError):
    code = "CHANNEL_ALREADY_EXISTS"
    status_code = 409

    def __init__(self, field: str):
        super().__init__(field=field)


class ChannelNotFoundError(AppError):
    code = "CHANNEL_NOT_FOUND"
    status_code = 404

    def __init__(self, channel_id: int):
        super().__init__(channel_id=channel_id)
