from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.exception.base import AppError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, e: AppError) -> JSONResponse:
        return JSONResponse(
            status_code=e.status_code,
            content={"code": e.code, **e.context},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_handler(request, e) -> JSONResponse:
        errors = [
            {
                "loc": err["loc"],
                "type": err["type"],
                "ctx": jsonable_encoder(err.get("ctx")),
            }
            for err in e.errors()
        ]
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"code": "VALIDATION_ERROR", "errors": errors},
        )
