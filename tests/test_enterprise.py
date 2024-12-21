from src.enterprise.domain_model import User
from src.enterprise.repository import (
    PersistenceUserRepository,
    CollectionUserRepository,
)
from src.enterprise.source import Memory
from src.enterprise.specification import (
    EmailUserSpecification,
    ActiveUserSpecification,
)
from src.enterprise.unit_of_work import MemoryUnitOfWork


def test_repository() -> None:
    email = "john@example.com"
    user = User(name="John Doe", email=email, hashed_password="")
    user.set_password("password")

    repository = PersistenceUserRepository(Memory({"User": {}}))
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


def test_uow() -> None:
    with MemoryUnitOfWork(Memory({"User": {}})) as uow:
        email = "john@example.com"
        user = User(name="John Doe", email=email, hashed_password="")
        user.set_password("password")

        repository = CollectionUserRepository(uow)
        repository.add(user)
        uow.commit()

        assert repository.get(user.id) == user
        assert repository.find(EmailUserSpecification(email)) == user

        repository.delete(user)
        uow.commit()

        assert repository.get(user.id) is None
