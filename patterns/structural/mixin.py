"""
Mixin is a design pattern that allows you to add additional functionality to classes through multiple inheritance.
Unlike base classes, mixins are not typically intended to be standalone objects. Instead, they are small classes that add specific functionality that can be “mixed”
into other classes to extend their capabilities.
"""

import json
from abc import ABC


class Jsonable(ABC):
    def json(self) -> str:
        return json.dumps(self)
