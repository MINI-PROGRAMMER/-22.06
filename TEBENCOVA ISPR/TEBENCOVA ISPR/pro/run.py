"""
Файл для запуска приложения.
Находится в корневой папке проекта.
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Запуск Fitness Center API...")
    print("📍 Документация: http://localhost:8000/docs")
    print("📍 ReDoc: http://localhost:8000/redoc")
    print("📍 Health: http://localhost:8000/health")
    print("-" * 50)

    uvicorn.run(
        "app.main:app",      # app - папка, main - файл, app - переменная FastAPI
        host="127.0.0.1",
        port=8000,
        reload=True
    )