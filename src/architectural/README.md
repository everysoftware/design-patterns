# Architectural Approaches

## Event-Sourcing

**Event Sourcing** is an architectural pattern in which each change in the state of a system is recorded as a
separate event. Instead of storing the current state of an object, the system stores the sequence of events that led to
that state. When necessary, the current state is restored by "replaying" the events in the order in which they occurred.

## CQRS

**Command Query Responsibility Segregation (CQRS)**, is a design pattern that divides the task of managing commands and
inquiries among several components. Separating
the methods for reading and publishing data is the primary goal of the CQRS architectural pattern. It separates the read
and update operations on a datastore into two separate models: Queries and Commands, respectively.

### CQS vs CQRS

Command Query Separation (CQS) and CQRS are related in that CQRS extends upon the fundamental concept of CQS. To put it
simply, this is how they are related:

* **CQS**: It is a programming principle that says you should separate operations that change data (commands) from those
  that read data (queries). If you have a method, for instance, it should either return something or update something,
  but not both.

* **CQRS**: By dividing the design of the entire system into two sections—one for managing commands (writing or
  modifying data) and another for managing queries (reading data), CQRS expands on this idea. Each side can have its
  own database or model to optimize how they work.
  So, CQS is the basic rule, and CQRS is like an advanced version of it used for bigger systems where you want to handle
  reading and writing differently.

## Vertical Slice

**Vertical Slice** is an architectural pattern that suggests that each feature should be implemented in its own slice
of the architecture. This means that each feature should have its own set of classes, including controllers, services,
and repositories. This pattern is useful for large applications that have many features, as it helps to keep the
codebase organized and maintainable.

## References

* [Implementing Domain-Driven Design Cheat Sheet](https://www.linkedin.com/pulse/implementing-domain-driven-design-cheat-sheet-saeed-farahi-mohassel/)
* [Repository - DDD in Ruby on Rails](https://www.visuality.pl/posts/repository-ddd-in-ruby-on-rails)
* [Многоликий DDD - YouTube](https://www.youtube.com/watch?v=NSN-NXfbEqM)
* [Паттерн CQRS — руководство для чайников - Tproger](https://tproger.ru/articles/cqrs-dlya-chajnikov)
* [CQRS – Command Query Responsibility Segregation Design Pattern - GeeksForGeeks](https://www.geeksforgeeks.org/cqrs-command-query-responsibility-segregation/)
