"""
Repository is an enterprise pattern that mediates between the domain and persistence layers using a collection-like
interface for accessing domain objects.

Content:
1. Collection-oriented vs persistence-oriented
2. Aggregate-centred (OrderRepository) vs Model-centred (OrderRepository and OrderItemRepository)
3. Specific (UserRepository) vs Generic (Repository<User>)
4. Transaction-dominant vs transaction-compliant.
5. Repository vs ORM Session vs DAO

1. Collection-oriented vs persistence-oriented

* Collection-oriented: can be thought as an in-memory set of entities which can track object changes.
Usually, you deal with this kind of repository when you are working with SQL databases and an ORM.
* Persistence-oriented: as a list or table of entities where you cannot track their changes.
You may have methods like save to abstract away details of how something is persisted.
Persistence-oriented repositories are more common in document (NoSQL) databases and an ODM.

2. Aggregate-centred (OrderRepository) vs Model-centred (OrderRepository and OrderItemRepository)

* Model-centred repository is considered an anti-pattern. The trouble with this approach is that it doesn't take into
account the consistency boundaries. E.g. if you have an Order model and an OrderItem model, you can't save
them separately, because they are part of the same aggregate. If you save them separately, you might end up with
inconsistent data.
* Aggregate-centred repository is the correct approach. It should be able to save the whole aggregate
at once. This way, you can ensure that the aggregate is always consistent.
* If you have a simple business logic, you might not need to use the repository pattern at all since there
is DAO pattern that can be used to access the database directly.

3. Specific (UserRepository) vs Generic (Repository<User>)

Generic repository is an a priori anti-pattern, since the repository encapsulates the logic of storing aggregates,
not a specific domain model. However, it is allowed to move the general functionality to the base class.

4. Transaction-dominant vs transaction-compliant.

The transaction management can not be the responsibility of the repository. It is the responsibility of the client
code to manage transactions. Therefore, transaction-dominant repositories are considered an anti-pattern.

5. Repository vs ORM Session vs DAO

Repository vs ORM Session:
ORM Session is more about data access, while Repository is more about business logic.
Repository may include pagination, filtering, caching, and other business logic, while ORM Session is more about
CRUD operations.

Repository vs DAO:
* DAO is any abstraction of data persistence. Repository is an abstraction of a collection of objects.
* DAO would be considered closer to the database, often table-centric.
Repository would be considered closer to the Domain, dealing only in Aggregate Roots.
* Repository could be implemented using DAO's, but you wouldn't do the opposite.
* It does seem common to see implementations called a Repository that is really more of a DAO,
and hence I think there is some confusion about the difference between them.

See more: https://dzone.com/articles/differences-between-repository-and-dao
"""

from abc import ABC, abstractmethod
from typing import Any

from src.enterprise.domain_model import User


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None: ...

    @abstractmethod
    def get(self, id: int) -> User | None: ...

    @abstractmethod
    def delete(self, user: User) -> None: ...

    @abstractmethod
    def find(self, specification: Any) -> User | None: ...
