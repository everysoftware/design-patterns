from src.enterprise.domain_model import User
from src.enterprise.repository import MemoryUserRepository
from src.enterprise.specification import (
    EmailUserSpecification,
    ActiveUserSpecification,
)


def test_repository() -> None:
    email = "john@example.com"
    user = User(name="John Doe", email=email, hashed_password="")
    user.set_password("password")

    repository = MemoryUserRepository()
    repository.add(user)

    assert repository.get(user.id) == user
    assert repository.find(EmailUserSpecification(email)) == user
    assert (
        repository.find(
            EmailUserSpecification(email) & ActiveUserSpecification()
        )
        == user
    )
    assert (
        repository.find(
            EmailUserSpecification(email) & ~ActiveUserSpecification()
        )
        is None
    )
    assert (
        repository.find(
            EmailUserSpecification(email) | ~ActiveUserSpecification()
        )
        == user
    )

    repository.delete(user)
    assert repository.get(user.id) is None
