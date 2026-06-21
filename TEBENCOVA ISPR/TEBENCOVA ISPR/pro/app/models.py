"""
Модели данных с валидацией через Pydantic.
Содержит модели для клиентов и тренеров.
"""
# Импортируем базовые классы Pydantic для создания моделей #  BaseModel - основа для всех моделей
# EmailStr - специальный тип, который проверяет формат email # field_validator - декоратор для написания своих правил проверки
from pydantic import BaseModel, EmailStr, field_validator

# Импортируем Optional - указывает, что поле может быть пустым (None)
from typing import Optional

# Импортируем UUID - тип для уникальных идентификаторов
from uuid import UUID

# Импортируем date - тип для работы с датами (год-месяц-день)
from datetime import date

# Импортируем Enum - для создания перечислений (списка допустимых значений)
from enum import Enum

# Импортируем re - библиотека для работы с регулярными выражениями (проверка текста по шаблону)
import re


class TrainerStatus(str, Enum):
    """Статусы тренера"""
    WORKING = "WORKING"             # Работает
    ON_LEAVE = "ON_LEAVE"           # В отпуске
    NOT_WORKING = "NOT_WORKING"     # Не работает


# ==================== МОДЕЛИ ТРЕНЕРА ====================

class TrainerCreate(BaseModel):
    """модель для создания тренера"""
    surname: str                                   # Фамилия 
    name: str                                      # Имя
    patronymic: Optional[str] = None               # Отчество
    phone: str                                     # Номер телефона
    status: TrainerStatus = TrainerStatus.WORKING  # Статус
    """настройка валидатора на фио"""
    @field_validator("surname", "name")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Поле не может быть пустым")
        return v.strip()
    """пописываем валдацию номера"""
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        cleaned = re.sub(r"[\s\-\(\)\+]", "", v)
        if not cleaned.isdigit() or not (7 <= len(cleaned) <= 15):
            raise ValueError("Некорректный номер телефона")
        return v


class TrainerUpdate(BaseModel):
    """Модель для обновления тренера"""
    surname: Optional[str] = None                # Фамилия
    name: Optional[str] = None                   # Имя
    patronymic: Optional[str] = None             # Отчество
    phone: Optional[str] = None                  # Номер телефона

    @field_validator("surname", "name")
    @classmethod
    def not_empty(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError("Поле не может быть пустым")
        return v.strip() if v else v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        cleaned = re.sub(r"[\s\-\(\)\+]", "", v)
        if not cleaned.isdigit() or not (7 <= len(cleaned) <= 15):
            raise ValueError("Некорректный номер телефона")
        return v


class TrainerStatusUpdate(BaseModel):
    """Модель для обновления статуса тренера"""
    status: TrainerStatus


class TrainerResponse(BaseModel):
    """Ответ с данными тренера"""
    id: UUID                                  # Уникальный идентификатор (генерируется сервером)
    surname: str                              # Фамилия
    name: str                                 # Имя
    patronymic: Optional[str]                 # Отчество
    phone: str                                # Номер телефона
    status: TrainerStatus                     # Статус


class TrainerShort(BaseModel):
    """Краткая информация о тренере (для вложения в клиента)"""
    id: UUID                                 # ID тренера
    name: str                                # Имя
    surname: str                             # Фамилия
    status: TrainerStatus                    # Статус


# ==================== МОДЕЛИ КЛИЕНТА ====================

class ClientCreate(BaseModel):
    """Модель для создания клиента"""
    surname: str
    name: str
    patronymic: Optional[str] = None
    birthday: date
    phone: str 
    email: str                             
    trainer_id: Optional[UUID] = None      

    """проверка заполнения поля клиента"""
    @field_validator("surname", "name")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Поле не может быть пустым")
        return v.strip()

    """валидация телефона клиента"""
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        cleaned = re.sub(r"[\s\-\(\)\+]", "", v)
        if not cleaned.isdigit() or not (7 <= len(cleaned) <= 15):
            raise ValueError("Некорректный номер телефона")
        return v

    """валидация почты клиента"""
    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(pattern, v):
            raise ValueError("Некорректный email адрес")
        return v.lower()

    """валидация дады рождения клиента"""
    @field_validator("birthday")
    @classmethod
    def validate_birthday(cls, v: date) -> date:
        if v >= date.today():
            raise ValueError("Дата рождения должна быть в прошлом")
        return v


class ClientUpdate(BaseModel):
    """Модель для обновления клиента"""
    surname: Optional[str] = None
    name: Optional[str] = None
    patronymic: Optional[str] = None
    birthday: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None

    @field_validator("surname", "name")
    @classmethod
    def not_empty(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError("Поле не может быть пустым")
        return v.strip() if v else v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        cleaned = re.sub(r"[\s\-\(\)\+]", "", v)
        if not cleaned.isdigit() or not (7 <= len(cleaned) <= 15):
            raise ValueError("Некорректный номер телефона")
        return v

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(pattern, v):
            raise ValueError("Некорректный email адрес")
        return v.lower()

    @field_validator("birthday")
    @classmethod
    def validate_birthday(cls, v: Optional[date]) -> Optional[date]:
        if v is not None and v >= date.today():
            raise ValueError("Дата рождения должна быть в прошлом")
        return v


class ClientStatusUpdate(BaseModel):
    """Модель для обновления статуса клиента"""
    is_active: bool


class ClientResponse(BaseModel):
    """Ответ с данными клиента"""
    id: UUID
    surname: str
    name: str
    patronymic: Optional[str]
    birthday: date
    phone: str
    email: str
    is_active: bool
    trainer_id: Optional[UUID]


class ClientDetailResponse(BaseModel):
    """Детальный ответ с данными клиента (с тренером)"""
    id: UUID
    surname: str
    name: str
    patronymic: Optional[str]
    birthday: date
    phone: str
    email: str
    is_active: bool
    trainer: Optional[TrainerShort]


class TrainerDetailResponse(BaseModel):
    """Детальный ответ с данными тренера (с клиентами)"""
    id: UUID
    surname: str
    name: str
    patronymic: Optional[str]
    phone: str
    status: TrainerStatus
    clients: list[ClientResponse]