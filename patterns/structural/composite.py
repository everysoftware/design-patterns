from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def as_string(self) -> str: ...


# Leaf
class File(Component):
    def __init__(self, name: str):
        self.name = name

    def as_string(self) -> str:
        return f"File: {self.name}"


# Composite
class Directory(Component):
    """
    Composite design pattern compose objects into tree structures to represent part-whole hierarchies.
    Composite lets clients treat individual objects and compositions of objects uniformly.
    """

    def __init__(self, name: str):
        self.name = name
        self.children: list[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def as_string(self) -> str:
        s = f"Directory: {self.name}\n"
        for child in self.children:
            s += f"{child.as_string()}\n"
        return s
