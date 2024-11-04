"""
The Hollywood Principle is a software development principle that states: “Don’t call us, we’ll call you.”
It suggests that high-level components should dictate the flow of control in an application, rather than low-level components.
This principle is often used in the context of inversion of control (IoC) and dependency inversion.

Dependency Inversion is the strategy of depending upon interfaces or abstract functions and classes rather than upon concrete functions and classes.
This is one of the SOLID principles.

Inversion of Control (IoC) is a general principle in which dependency management is delegated to a system or external component, rather than being performed by the object itself.
In this approach, an object does not create its dependencies itself, but receives them from the outside, which is often implemented through DI.
IoC allows for reduced coupling between components and simplifies testing and replacing individual parts of the system.

IoC can be implemented using different patterns: Dependency Injection, Event-driven Architecture (when actions are triggered by events) and
Service Locator (searching for the required component in a global service).

All these patterns help to achieve the Low Coupling and High Cohesion principles, which are essential for building maintainable and scalable software.
"""
