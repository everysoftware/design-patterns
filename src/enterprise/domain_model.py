"""
Domain Model (Entity) is an enterprise design pattern that describes the object model of the problem domain. The domain model
is a representation of meaningful real-world concepts pertinent to the domain that need to be modeled in software.
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
