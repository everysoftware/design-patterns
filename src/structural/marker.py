"""
Marker is a structural design pattern used to "mark" (or "label") classes, allowing them to be distinguished by certain
characteristics without adding new methods or fields.

Unlike other interfaces, a marker interface does not itself contain any functionality -
it simply serves as an indication that the class implementing it has certain characteristics or purpose.
"""

from typing import Any


class Marker:
    def __init__(self, label: str):
        self.label = label

    def __call__[T](self, marked: T) -> T:
        setattr(marked, f"{self.label}_mark", True)
        return marked

    def is_marked(self, marked: Any) -> bool:
        return hasattr(marked, f"{self.label}_mark")


loggable = Marker("loggable")
