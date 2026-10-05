class AppError(Exception):
    code: str = "APP_ERROR"
    status_code: int = 500

    def __init__(self, **context):
        self.context = context
        super().__init__(self.code)
