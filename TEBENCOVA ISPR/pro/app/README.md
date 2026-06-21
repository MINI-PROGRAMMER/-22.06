# Fitness Center REST API

## Технологии

- **Python 3.11+**
- **FastAPI** — веб-фреймворк
- **Pydantic v2** — валидация данных
- **Uvicorn** — ASGI-сервер
- **Хранилище** — in-memory (dict в оперативной памяти)

## Запуск

```bash
pip install -r requirements.txt

python run.py
```


Документация Swagger: http://localhost:8000/docs

---

## API Endpoints

### Клиенты `/api/clients`

| Метод  | Путь                                           | Описание                          |
|--------|------------------------------------------------|-----------------------------------|
| POST   | `/api/clients`                                 | Создать клиента                   |
| PUT    | `/api/clients/{id}`                            | Обновить данные клиента           |
| GET    | `/api/clients`                                 | Список всех клиентов              |
| GET    | `/api/clients/{id}`                            | Краткая информация о клиенте      |
| GET    | `/api/clients/{id}/detail`                     | Подробная информация с тренером   |
| PATCH  | `/api/clients/{id}/status`                     | Активировать / деактивировать     |
| POST   | `/api/clients/{clientId}/trainer/{trainerId}`  | Назначить тренера                 |

### Тренеры `/api/trainers`

| Метод  | Путь                          | Описание                                 |
|--------|-------------------------------|------------------------------------------|
| POST   | `/api/trainers`               | Создать тренера                          |
| PUT    | `/api/trainers/{id}`          | Обновить данные тренера                  |
| PATCH  | `/api/trainers/{id}/status`   | Изменить статус тренера                  |
| GET    | `/api/trainers`               | Список всех тренеров                     |
| GET    | `/api/trainers/{id}/detail`   | Подробная информация со списком клиентов |

---

## Модели данных

### Client
```json
{
  "surname": "Кобяков",
  "name": "Олег",
  "patronymic": "Владимироваич",
  "birthday": "1992-29-02",
  "phone": "+7 902 299 92 29",
  "email": "ivan@example.com",
  "trainer_id": null
}
```

### Trainer
```json
{
  "surname": "Пупкин",
  "name": "Петр",
  "patronymic": "Пантович",
  "phone": "+7 909 989 98 99",
  "status": "WORKING"
}
```

Статусы тренера: `WORKING` | `ON_LEAVE` | `NOT_WORKING`

---

## Коды ответов

| Код | Описание                     |
|-----|------------------------------|
| 201 | Ресурс успешно создан        |
| 200 | Успешный запрос              |
| 400 | Ошибка валидации             |
| 404 | Ресурс не найден             |

## Структура проекта


PROIZBOD/                              ← ГЛАВНАЯ ПАПКА (ОТКРОЙ ЕЁ В VS CODE)
│
├── app/                               ← ПАПКА С КОДОМ
│   ├── __init__.py                    ← ПУСТОЙ ФАЙЛ (ОБЯЗАТЕЛЬНО!)
│   ├── main.py                        ← ГЛАВНЫЙ ФАЙЛ
│   ├── models.py                      ← МОДЕЛИ ДАННЫХ
│   ├── storage.py                     ← ХРАНИЛИЩЕ
│   └── routers/                       ← ПАПКА С МАРШРУТАМИ
│       ├── __init__.py                ← ПУСТОЙ ФАЙЛ (ОБЯЗАТЕЛЬНО!)
│       ├── clients.py                 ← ЭНДПОИНТЫ КЛИЕНТОВ
│       └── trainers.py                ← ЭНДПОИНТЫ ТРЕНЕРОВ
│
├── requirements.txt                   ← ЗАВИСИМОСТИ (ОБЯЗАТЕЛЬНО!)
└── run.py                             ← ЗАПУСК (ОБЯЗАТЕЛЬНО!)
