"""
Flyweight is a structural pattern used to efficiently manage large numbers of small objects.
The basic idea is to separate an object's state into internal and external, minimizing memory usage by
sharing common data.
"""

from typing import MutableMapping


class Character:
    def __init__(self, character_type: str) -> None:
        self.character_type = character_type

    @staticmethod
    def render(color: str, x: int, y: int) -> str:
        return f"Soldier at ({x}, {y}) with color {color}"


class FlyweightFactory:
    def __init__(self) -> None:
        self.characters: MutableMapping[str, Character] = {}

    def get_character(self, character_type: str) -> Character:
        if character_type not in self.characters:
            self.characters[character_type] = Character(character_type)
        return self.characters[character_type]
