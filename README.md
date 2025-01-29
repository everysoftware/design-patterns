# System Design

Well-designed systems are easy to maintain, easy to understand, and easy to change. They're also easy to scale, easy to
test, and easy to debug. The principles of software design are timeless, but they're also constantly evolving. This
repository contains a collection of design patterns, principles, and best practices for building software systems.

## Content

1. Principles of Design
2. Creational Patterns
3. Structural Patterns
4. Behavioral Patterns
5. Concurrency Patterns
6. Enterprise Patterns

## Principles of Design

| #  | Principle          | Decoding                                                                                             |
|----|--------------------|------------------------------------------------------------------------------------------------------|
| 1  | [DRY]()            | Don't Repeat Yourself                                                                                |
| 2  | [KISS]()           | Keep It Simple, Stupid                                                                               |
| 3  | [YAGNI]()          | You Aren't Gonna Need It                                                                             |
| 4  | [OOP principles]() | Object-Oriented Programming                                                                          |
| 5  | [SOLID]()          | Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| 6  | [Hollywood]()      | Don't Call Us, We'll Call You                                                                        |
| 7  | [ACID]()           | Atomicity, Consistency, Isolation, Durability                                                        |
| 8  | [CQS]()            | Command Query Separation                                                                             |
| 9  | [GRASP]()          | General Responsibility Assignment Software Patterns                                                  |
| 10 | [12 Factor App]()  | Methodology for building SaaS applications                                                           |

## Creational Patterns

| #  | Pattern                  | Description                                                                                                                                     |
|----|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Creational Method]()    | Simple wrapper method over the item constructor call                                                                                            |
| 2  | [Simple Factory]()       | Define a class for creating objects without subclassing                                                                                         |
| 3  | [Factory Method]()       | Define an interface for creating an object, but let subclasses decide which class to instantiate                                                |
| 4  | [Abstract Factory]()     | Provide an interface for creating families of related or dependent objects without specifying their concrete classes                            |
| 5  | [Builder]()              | Separate the construction of a complex object from its representation, allowing the same construction process to create various representations |
| 6  | [Prototype]()            | Creating an object by cloning another object instead of creating it through a constructor to avoid costly creation steps                        |
| 7  | [Singleton]()            | Ensure a class has only one instance and provide a global point of access to it                                                                 |
| 8  | [Multiton]()             | Ensure a class has named instances, and provide a global point of access to them                                                                |
| 9  | [Monostate]()            | Ensure that all instances of a class share the same state                                                                                       |
| 10 | [Lazy Initialization]()  | Delay the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed                  |
| 11 | [RAII]()                 | Ensure resources are properly acquired and released                                                                                             |
| 12 | [Object Pool]()          | Reuse and share objects that are expensive to create                                                                                            |
| 13 | [Dependency Injection]() | A class accepts the objects it requires from an injector instead of creating the objects directly                                               |

## Structural Patterns

| #  | Pattern             | Description                                                                                                                                                           |
|----|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Adapter]()         | Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces |
| 2  | [Bridge]()          | Decouple an abstraction from its implementation so that the two can vary independently                                                                                |
| 3  | [Composite]()       | Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly       |
| 4  | [Decorator]()       | Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality                     |
| 5  | [Facade]()          | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use                     |
| 6  | [Flyweight]()       | Use sharing to support large numbers of fine-grained objects efficiently                                                                                              |
| 7  | [Proxy]()           | Provide a surrogate or placeholder for another object to control access to it                                                                                         |
| 8  | [Service Locator]() | Provide a centralized registry for obtaining services without the need for hard-coded references to their implementations                                             |
| 9  | [Marker]()          | Add a special marker interface to a class to provide metadata about the class                                                                                         |
| 10 | [Mixin]()           | Add functionality to a class by subclassing                                                                                                                           |
| 11 | [Delegate]()        | Pass on the responsibility for a task to another class                                                                                                                |

## Behavioral Patterns

| #  | Pattern                     | Description                                                                                                                                                                                                       |
|----|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Chain of Responsibility]() | Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it |
| 2  | [Command]()                 | Encapsulate a request as an object, thereby allowing for parameterization of clients with different requests, queuing of requests, and logging of requests                                                        |
| 3  | [Interpreter]()             | Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language                                                           |
| 4  | [Iterator]()                | Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation                                                                                           |
| 5  | [Mediator]()                | Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly                                                     |
| 6  | [Memento]()                 | Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later                                                                        |
| 7  | [Observer]()                | Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically                                                                  |
| 8  | [State]()                   | Allow an object to alter its behavior when its internal state changes. The object will appear to change its class                                                                                                 |
| 9  | [Strategy]()                | Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients                                                                   |
| 10 | [Template Method]()         | Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure        |
| 11 | [Visitor]()                 | Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates                          |
| 12 | [Null Object]()             | Provide an object as a surrogate for the lack of an object of a given type. Null Object provides intelligent do-nothing behavior, hiding the details from its collaborators                                       |
| 13 | [Retry]()                   | Retry a failed operation a certain number of times with a certain delay between retries                                                                                                                           |
| 14 | [Servant]()                 | Create a class that performs specific actions for a group of other classes without being part of them                                                                                                             |
| 15 | [Session]()                 | Define an object that acts as a container for storing data or state required to perform various operations within a single session                                                                                |
| 16 | [Generator]()               | Generate objects in a way that allows the client to control the generation process                                                                                                                                |
| 17 | [Timeout]()                 | Limit the time a process or a thread is allowed to run                                                                                                                                                            |
| 18 | [Caching]()                 | Store data in a cache to reduce the number of requests to an external service                                                                                                                                     |
| 19 | [Throttling]()              | Control the rate of requests sent or received by a service                                                                                                                                                        |

## Concurrency Patterns

| # | Pattern        | Description                                                                                                             |
|---|----------------|-------------------------------------------------------------------------------------------------------------------------|
| 1 | [Future]()     | A pattern that represents the result of an asynchronous operation                                                       |
| 2 | [Coroutine]()  | A pattern that allows a function to be paused and resumed at a later time without blocking the execution of the program |
| 3 | [Event Loop]() | A pattern that waits for and dispatches events or messages in a program                                                 |
| 4 | [Mutex]()      | A pattern that ensures that only one thread can access a resource at a time                                             |
| 6 | [Semaphore]()  | A pattern that restricts the number of threads that can access a resource at a time                                     |
| 7 | [Barrier]()    | A pattern that allows multiple threads to wait for each other at a predefined point in the program                      |

## Enterprise patterns

| #  | Pattern                  | Description                                                                                                                                                                     |
|----|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Domain Model]()         | An object model of the domain that incorporates both behavior and data                                                                                                          |
| 2  | [Data Mapper]()          | A layer of Mappers that moves data between objects and a database while keeping them independent of each other                                                                  |
| 3  | [Active Record]()        | An object that wraps a row in a database table or view, encapsulates the database access, and adds domain logic on that data                                                    |
| 4  | [Data Access Object]()   | An object that provides an abstract interface to some type of database or other persistence mechanism                                                                           |
| 5  | [Value Object]()         | An object that contains attributes but has no conceptual identity. They should be treated as immutable                                                                          |
| 6  | [Aggregate]()            | A collection of objects that are bound together by a root entity, ensuring that changes to the root propagate to the entire collection                                          |
| 7  | [Repository]()           | Mediate between the domain and data mapping layers using a collection-like interface for accessing domain objects                                                               |
| 8  | [Specification]()        | Recombinable business logic in a boolean fashion. Specification is a pattern that allows you to combine rules to create more complex rules, which you can use to filter objects |
| 9  | [Identity Map]()         | Ensure that each object gets loaded only once by keeping every loaded object in a map. Looks up objects using the map when referring to them                                    |
| 10 | [Unit of Work]()         | Maintain a list of objects affected by a business transaction and coordinates the writing out of changes and the resolution of concurrency problems                             |
| 11 | [Data Transfer Object]() | An object that carries data between processes. The data transfer object is not tied to any specific operation and does not have any behavior                                    |
