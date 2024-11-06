"""
Servant is a behavioral design pattern that allows you to create a class that performs specific actions for a group
of other classes without being part of them. The Servant pattern provides a helper object (or service) that performs
common functions for one or more classes, thereby reducing code duplication and promoting reuse.
"""

from abc import ABC


class GraphicObject(ABC):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Circle(GraphicObject):
    pass


class Square(GraphicObject):
    pass


# Servant
class Mover:
    @staticmethod
    def move(obj: GraphicObject, dx: float, dy: float) -> None:
        obj.x += dx
        obj.y += dy
