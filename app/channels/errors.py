class ChannelAlreadyExistsError(Exception):
    code = "CHANNEL_ALREADY_EXISTS"

    def __init__(self, field: str):
        self.field = field


class UserNotFoundError(Exception):
    code = "CHANNEL_NOT_FOUND"

    def __init__(self, channel_id: int):
        self.channel_id = channel_id
