from app.core.exception.base import AppError


class InvalidCredentialsError(AppError):
    code = "INVALID_CREDENTIALS"
    status_code = 401


class InvalidTokenError(AppError):
    code = "INVALID_TOKEN"
    status_code = 401
