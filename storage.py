"""
In-memory хранилище данных.
Данные хранятся в словарях в оперативной памяти.
"""

from uuid import UUID
from typing import Optional
from datetime import date


# Словари для хранения данных
trainers: dict[UUID, dict] = {}
clients: dict[UUID, dict] = {}


# ==================== РАБОТА С ТРЕНЕРАМИ ====================

def get_all_trainers() -> list[dict]:
    """Получить список всех тренеров"""
    return list(trainers.values())


def get_trainer_by_id(trainer_id: UUID) -> Optional[dict]:
    """Получить тренера по ID"""
    return trainers.get(trainer_id)


def create_trainer(trainer: dict) -> dict:
    """Создать тренера"""
    trainers[trainer["id"]] = trainer
    return trainer


def update_trainer(trainer_id: UUID, updates: dict) -> Optional[dict]:
    """Обновить данные тренера"""
    if trainer_id not in trainers:
        return None
    trainers[trainer_id].update(updates)
    return trainers[trainer_id]


# ==================== РАБОТА С КЛИЕНТАМИ ====================

def get_all_clients() -> list[dict]:
    """Получить список всех клиентов"""
    return list(clients.values())


def get_client_by_id(client_id: UUID) -> Optional[dict]:
    """Получить клиента по ID"""
    return clients.get(client_id)


def create_client(client: dict) -> dict:
    """Создать клиента"""
    clients[client["id"]] = client
    return client


def update_client(client_id: UUID, updates: dict) -> Optional[dict]:
    """Обновить данные клиента"""
    if client_id not in clients:
        return None
    clients[client_id].update(updates)
    return clients[client_id]


def get_clients_by_trainer(trainer_id: UUID) -> list[dict]:
    """Получить всех клиентов, закреплённых за тренером"""
    return [c for c in clients.values() if c.get("trainer_id") == trainer_id]