# Описание класса животное

__all__ = ["Animal"]


class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        """Основной способ передвижения"""
        pass

    def say(self):
        """Способ общения, производимые звуки"""
        pass

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.age}"