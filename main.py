"""
Главный файл приложения.
Запускает сервер FastAPI с документацией Swagger.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .routers import clients, trainers

# Создаём приложение
app = FastAPI(
    title="Fitness Center API",
    description="REST API для управления фитнес-центром",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(clients.router)
app.include_router(trainers.router)


# Обработчик ошибок валидации (400)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = " -> ".join(str(loc) for loc in error["loc"] if loc != "body")
        errors.append({"field": field, "message": error["msg"]})
    return JSONResponse(status_code=400, content={"detail": errors})


# ==================== ДОПОЛНИТЕЛЬНЫЕ ЭНДПОИНТЫ ====================

@app.get("/")
def root():
    """Приветственное сообщение"""
    return {
        "message": "Fitness Center API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """Проверка работоспособности сервера"""
    return {"status": "ok"}


# ==================== ЗАПУСК ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",          # Имя файла и переменная app
        host="127.0.0.1",    # Адрес
        port=8000,           # Порт
        reload=True          # Автоперезагрузка при изменениях
    )