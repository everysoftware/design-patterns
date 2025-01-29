# Enterprise Design Patterns

## Table of contents

* [Value Object](#value-object)
* [Domain Model](#domain-model)
* [Aggregate](#aggregate)
* [Data Mapper](#data-mapper)
* [Active Record](#active-record)
* [Data Access Object](#data-access-object)
* [Repository](#repository)
* [Specification](#specification)
* [Identity Map](#identity-map)
* [Unit of Work](#unit-of-work)
* [Sources](#sources)

## Value Object

**Value Object** is an enterprise design pattern that is used to represent objects that are characterized by their state
(value) rather than identity. This pattern is used to model simple entities that have a value
and do not have an identity of their own.

### Properties

* **Value-based**: Two objects are considered equal if all their attributes are equal.
* **Immutability**: Value Objects are usually immutable once created.
* **Modeling Usage**: Value Objects are used to model concepts that are easily defined by their attributes, such as
  money,
  addresses, coordinates, etc.

## Domain Model

**Domain Model** is an enterprise design pattern that describes the object model of the problem domain.
The domain model is a representation of meaningful real-world concepts pertinent to the domain that need to be modeled
in software.

* **Anemic** Domain Model is an antipattern where the domain model contains only data and no behavior. The behavior is
  implemented in services. This is an antipattern because it violates the object-oriented principle of encapsulation.

* **Rich** Domain Model is an enterprise design pattern where the domain model contains both data and behavior. The
  behavior
  is implemented in the domain model itself. This is a good practice because it adheres to the object-oriented principle
  of encapsulation.

## Aggregate

**Aggregate** is an enterprise design pattern that represents the group of dependant domain models.
The main goal is to organize objects, ensure data integrity, and manage complex relationships so that
they remain consistent.

### Properties

* **Root Entity**: An aggregate has a root entity, which is the access point to all other objects in the aggregate.
* **Coupled entities**: All objects within an aggregate are tightly coupled and should be considered a single logical
  unit.
* **Data Integrity**: Changes within an aggregate must be made through the root entity to maintain data integrity.

Domain model can be considered as an aggregate if it satisfies the conditions above, e.g. User.

## Data Mapper

**Data Mapper** (Persistence/ORM model) is an enterprise design pattern that maps objects to database tables.

### Can Data Mapper be used as Domain Model?

In DDD you have the domain model and the repository. That's it! If inside the repository you will persist the domain
model directly OR if you will convert it to a persistence model before persisting it, it's up to you! It's a matter of
design, your design. The domain doesn't care about how models are saved. It's an implementation detail of the
repository, and it doesn't matter for the domain. That's the entire purpose of Repositories: encapsulate persistence
logic & details inside it.

But as developers we know it's not always possible to build a domain 100% immune from persistence interference, even
they being different things.

### Why this can be a good idea?

* **Avoiding duplicated code**: you can use the same model for the domain and the persistence layer.
* **Performance**: due to shorten the number of mapping operations, the persistence model can be more efficient.
* **Take everything from ORM**: relationships, lazy loading, change tracking, and cascading are become easier to
  implement.

### Why this can be a problem?

* **ORM dependency**: our code becomes dependent on the ORM. If we decide to change the ORM, we will have to change the
  domain model. (_How often do you change the ORM?_)
* **SRP violation**: the domain model is designed to be a representation of the business rules
  and logic. The persistence model is designed to be a representation of the database schema. (_Is your domain model
  just a mirror of the database schema? There are always victims, whether it SRP or DRY violation_)
* **Consistency**: we usually work with aggregates to ensure consistency and invariants. The persistence model is just
  a representation of one table, and it doesn't have the same constraints as the domain model. (_You can use the
  relationships, custom properties, and methods to ensure consistency, so it's not a big deal_)

### What is the best approach?

It depends on your project. And not the size of the project, but the complexity of the domain. If you have a
really complex business rules, it's better to separate the domain model from the persistence model. But it is not a
necessity or a silver bullet that will solve all your problems. I guess the best approach is to start with a single
model and refactor it when you feel the need. It's better to have a working code than a perfect code that doesn't
work.

## Active Record

**Active Record** is an enterprise design pattern that allows you to store and retrieve data in a database using
objects.

## Data Access Object

> **Data Access Object** (DAO) pattern comes from **early enterprise application design**, and its
> formalization can be found in the book "Core J2EE Patterns: Best Practices and Design Strategies" by Deepak Alur, John
> Crupi, and Dan Malks, published in 2001. DAO abstracts and encapsulates all access to a data source, separating
> persistence logic from business logic. This allows changes to the underlying data source without affecting the rest of
> the application, which is especially useful in enterprise contexts where systems might switch databases or data
> storage
> mechanisms over time.

**DAO** (Data Access Object) is an enterprise pattern that is used as abstraction of data persistence.

## Repository

> The **Repository** pattern originates from **Domain-Driven Design** (DDD), as described by Eric Evans in his book, "
> Domain-Driven Design: Tackling Complexity in the Heart of Software." (2003) Repositories are not just about managing
> data; they encapsulate business logic, ensuring that operations adhere to the Ubiquitous Language of the domain.

**Repository** is an enterprise pattern that mediates between the domain and persistence layers using a collection-like
interface for accessing domain objects.

* **Collection-like repository**: can be thought as an in-memory set of entities which can track object changes.
  Usually, you deal with this kind of repository when you are working with SQL databases and an ORM.

* **Persistence-oriented repository**: as a list or table of entities where you cannot track their changes.
  Persistence-oriented repositories are more common in document (NoSQL) databases and an ODM.

Best practices:

1. **Don't use generic repository**. Generic repository is an a priori anti-pattern, since the repository encapsulates
   the logic of storing aggregates,
   not a specific domain model. However, it is allowed to move the general functionality to the base class.
2. **Manage transactions outside the repository**. The transaction management can not be the responsibility of the
   repository. It is the responsibility of the client
   code to manage transactions.
3. **Focus on aggregates, not entities**. E.g. you can't save Order and OrderItem separately, because they are part of
   the
   same aggregate. Otherwise, you might end up with inconsistent data.

| Criterion                  | Repository                                            | Data Access Object (DAO)                           | ORM Session                                         |
|----------------------------|-------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|
| **Main Idea**              | Abstraction over a collection of domain model objects | Abstraction for working with a data source         | Object managing ORM transactions and sessions       |
| **Level of Abstraction**   | High (works with domain objects)                      | Medium (works with database objects)               | Low (works with specific SQL queries via ORM)       |
| **ORM Dependency**         | Not tied to ORM (but can use it)                      | Can use ORM, JDBC, ADO.NET, and other technologies | Part of ORM (e.g., SQLAlchemy, Hibernate)           |
| **Focus**                  | Business logic and working with aggregates            | Encapsulation of CRUD operations                   | Managing connections and transactions               |
| **Where Used**             | DDD (Domain-Driven Design), complex systems           | Smaller projects, clean architecture               | ORM frameworks (SQLAlchemy, Hibernate)              |
| **Flexibility**            | High, can switch between data sources                 | Medium, requires adaptation for a data source      | Low, tightly coupled with ORM                       |
| **Ease of Testing**        | High, easily mockable                                 | Medium, testing is possible                        | Low, requires mocks or a test database              |
| **Example Implementation** | `UserRepository.get_active_users()`                   | `UserDAO.get_user_by_id(id)`                       | `session.query(User).filter(User.id == id).first()` |

## Specification

**Specification** is an enterprise design pattern that use to describe recombinable business logic in a boolean fashion.
Moreover, this pattern that allows you to combine rules to create more complex rules, which you can use to filter
objects

### Use cases

* **Finding data in the database**. This is finding records that match certain criteria.
* **Checking objects in memory**. In other words, checking that the object we retrieved from the DB matches the
  specification.
* **Creating a new instance that matches the criteria**. This is useful in cases where you don't care about the actual
  contents of the instances, but still need to have certain attributes.

### Identity Map

**Identity Map** is an enterprise design pattern used to manage the identity of objects in a data-driven application.
Its main purpose is to ensure that each object loaded from the database has only one unique copy in the application.

### Use cases

* **Object caching**: When an object is requested, Identity Map first checks if it already exists in memory (in the
  cache)
  for the current session or transaction. If the object is already loaded, then that copy is returned instead of
  creating a new instance.

* **Maintaining data integrity**: This prevents the problem of the same object being loaded multiple times and each
  instance having its own state. Instead, all changes to the object will be reflected in a single instance.

* **Speeding up data**: Since Identity Map stores already loaded objects in the cache, it reduces the need for
  repeated database hits, improving performance.

## Unit of Work

**Unit of Work** is an enterprise design pattern that maintains a list of objects affected by a business transaction.
It coordinates the writing out of changes and the resolution of concurrency problems.

## References

* [Domain Model - Martin Fowler](https://martinfowler.com/eaaCatalog/domainModel.html)
* [Aggregate - Martin Fowler](https://martinfowler.com/bliki/DDD_Aggregate.html)
* [Data Mapper - Martin Fowler](https://martinfowler.com/eaaCatalog/dataMapper.html)
* [Active Record - Martin Fowler](https://martinfowler.com/eaaCatalog/activeRecord.html)
* [Repository - Martin Fowler](https://martinfowler.com/eaaCatalog/repository.html)
* [Specification - Martin Fowler](https://martinfowler.com/apsupp/spec.pdf)
* [Identity Map - Martin Fowler](https://martinfowler.com/eaaCatalog/identityMap.html)
* [Unit of Work - Martin Fowler](https://martinfowler.com/eaaCatalog/unitOfWork.html)
* [Differnces between repository and DAO - DZone](https://dzone.com/articles/differences-between-repository-and-dao)
* [Repository DDD in Ruby on rails - Visuality](https://www.visuality.pl/posts/repository-ddd-in-ruby-on-rails)
* [What is a Repository - ShawnMc.Cool](https://shawnmc.cool/what-is-a-repository)
* [Паттерн проектирования Спецификация - Bool](https://jopr-site.azureedge.net/blog/detail/spetsifikatsiya-pattern-proektirovaniya)
* [Implementing a Unit of Work - SitePoint](https://www.sitepoint.com/implementing-a-unit-of-work/)
* [The Unit of Work Design Pattern Explained](https://www.youtube.com/watch?v=HX6vkP-QD7U)
* [Unit of Work: от простого к сложному](https://www.youtube.com/watch?v=oP_OUiIK4Rc)
