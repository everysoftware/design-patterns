"""
Memento is a behavioral design pattern that allows saving and restoring the state of an object without
breaking encapsulation. This is achieved by creating a "snapshot" of the object's state at a certain point in time,
allowing it to be restored to the same state later.

The basic idea is to separate the process of storing the object's state from the object, so that the object can focus
on its core logic, and saving and restoring the state is done through a special Memento class. The pattern is often
used in scenarios where it is necessary to provide the ability to roll back changes
(for example, in text editors or games).
"""


class Snapshot:
    def __init__(self, state: str) -> None:
        self.state = state


class Object:
    def __init__(self, state: str) -> None:
        self.state = state

    def save(self) -> Snapshot:
        return Snapshot(self.state)

    def restore(self, snap: Snapshot) -> None:
        self.state = snap.state

    def set_state(self, state: str) -> None:
        self.state = state

    def get_state(self) -> str:
        return self.state


class Caretaker:
    def __init__(self) -> None:
        self.snapshots: list[Snapshot] = []

    def add(self, snap: Snapshot) -> None:
        self.snapshots.append(snap)

    def get(self, index: int) -> Snapshot:
        return self.snapshots[index]
