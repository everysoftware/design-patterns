import json
from abc import ABC
from typing import Self


class Jsonable(ABC):
    def json(self) -> str:
        return json.dumps(self)

    @classmethod
    def from_json(cls, data: str) -> Self:
        """
        Creational Method is a simple wrapper method over the item constructor call.
        The create method helps isolate any changes to the product construction from the main code.
        """
        try:
            dct = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Data must be a valid JSON string")
        if not isinstance(dct, dict):
            raise ValueError("JSON must represent an object")
        return cls(**dct)  # noqa
