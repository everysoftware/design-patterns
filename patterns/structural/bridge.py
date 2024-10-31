from abc import abstractmethod, ABC


# Implementor
class OperatingSystem(ABC):
    @abstractmethod
    def boot(self) -> str: ...

    @abstractmethod
    def shutdown(self) -> str: ...


class WindowsOS(OperatingSystem):
    def boot(self) -> str:
        return "Windows loading..."

    def shutdown(self) -> str:
        return "Windows shutting down."


class LinuxOS(OperatingSystem):
    def boot(self) -> str:
        return "Linux loading..."

    def shutdown(self) -> str:
        return "Linux shutting down."


# Abstraction
class Device(ABC):
    """
    Bridge is a structural design pattern that decouples abstraction and implementation, allowing them to be modified independently.
    This is especially useful when new variations of an abstraction and its implementation are introduced,
    and it is necessary to avoid "cartesian" (or "combinatorial") class explosion.

    In this example, the Device abstraction is decoupled from the OperatingSystem implementation.
    If we add a new device (e.g. Tablet) or a new OS (e.g. macOS), we can easily create new classes without modifying existing code.
    Otherwise, we would have to create a new class for each combination of device and OS.
    """

    def __init__(self, os: OperatingSystem) -> None:
        self.os = os

    def power_on(self) -> str: ...
    def power_off(self) -> str: ...


class Computer(Device):
    def power_on(self) -> str:
        return f"Computer: {self.os.boot()}"

    def power_off(self) -> str:
        return f"Computer: {self.os.shutdown()}"


class Smartphone(Device):
    def power_on(self) -> str:
        return f"Smartphone: {self.os.boot()}"

    def power_off(self) -> str:
        return f"Smartphone: {self.os.shutdown()}"
