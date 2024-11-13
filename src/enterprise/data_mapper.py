"""
Data mapper (Persistence/ORM model) is an enterprise design pattern that maps objects to database tables.

PERSISTENCE MODEL vs DOMAIN MODEL

In DDD you have the domain model and the repository. That's it! If inside the repository you will persist the domain
model directly OR if you will convert it to a persistence model before persisting it, it's up to you! It's a matter of
design, your design. The domain doesn't care about how models are saved. It's an implementation detail of the
repository, and it doesn't matter for the domain. That's the entire purpose of Repositories: encapsulate persistence
logic & details inside it.

But as developers we know it's not always possible to build a domain 100% immune from persistence interference, even
they being different things.

Why this can be a good idea?

* Avoiding duplicated code: you can use the same model for the domain and the persistence layer.
* Performance: due to shorten the number of mapping operations, the persistence model can be more efficient.
* Take everything from ORM: relationships, lazy loading, change tracking, and cascading are become easier to implement.

Why this can be a problem?

* ORM dependency: our code becomes dependent on the ORM. If we decide to change the ORM, we will have to change the
domain model. (How often do you change the ORM?)
* SRP violation: the domain model is designed to be a representation of the business rules
and logic. The persistence model is designed to be a representation of the database schema. (Is your domain model
just a mirror of the database schema? There are always victims, whether it SRP or DRY violation)
* Consistency: we usually work with aggregates to ensure consistency and invariants. The persistence model is just
a representation of one table, and it doesn't have the same constraints as the domain model. (You can use the
relationships, custom properties, and methods to ensure consistency, so it's not a big deal)

What is the best approach?

It depends on your project. And not the size of the project, but the complexity of the domain. If you have a
really complex business rules, it's better to separate the domain model from the persistence model. But it is not a
necessity or a silver bullet that will solve all your problems. I guess the best approach is to start with a single
model and refactor it when you feel the need. It's better to have a working code than a perfect code that doesn't work.
"""

from typing import Any


class Column[T]:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...


class User:
    id: Column[int] = Column(auto_increment=True, primary_key=True)
    name: Column[str] = Column()
    email: Column[str] = Column()
    hashed_password: Column[str] = Column()
