"""
Domain Model (Entity) is an enterprise design pattern that describes the object model of the problem domain. The domain model
is a representation of meaningful real-world concepts pertinent to the domain that need to be modeled in software.

Anemic Domain Model is an antipattern where the domain model contains only data and no behavior. The behavior is
implemented in services. This is an antipattern because it violates the object-oriented principle of encapsulation.

Rich Domain Model is an enterprise design pattern where the domain model contains both data and behavior. The behavior
is implemented in the domain model itself. This is a good practice because it adheres to the object-oriented principle
of encapsulation.
"""

import hashlib
import uuid
from dataclasses import dataclass, field


@dataclass
class Entity:
    id: int = field(default_factory=lambda: uuid.uuid4().int)


@dataclass(kw_only=True)
class User(Entity):
    name: str
    email: str
    hashed_password: str
    is_active: bool = True

    def verify_password(self, password: str) -> bool:
        return (
            hashlib.sha256(password.encode()).hexdigest()
            == self.hashed_password
        )

    def set_password(self, password: str) -> None:
        self.hashed_password = hashlib.sha256(password.encode()).hexdigest()
