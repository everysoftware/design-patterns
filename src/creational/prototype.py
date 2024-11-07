"""
Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.
Simply put, it is a pattern of creating an object by cloning another object instead of creating it through a constructor.

Use:
* When creating new objects is more complex or costly than copying existing ones. Cloning can be more efficient if significant resources are needed.
* For managing various objects with minor differences. Instead of creating multiple classes, you can clone and modify prototypes.
* For dynamic configurations where you need to create objects at runtime. You can clone a base configuration and adjust it as necessary.
* Can lower initialization costs, as cloning is often faster than building a new object from scratch, especially if initialization is resource-intensive.

Prototype pattern is available in Python out of the box with a copy module:

copy.copy() - Shallow copy
A shallow copy replicates the top-level structure of an object but does not create copies of its nested objects.

copy.deepcopy() - Deep copy
In contrast, a deep copy replicates both the top-level structure and all nested objects, creating entirely independent copies.

Shallow copying is often faster and more straightforward, but it can lead to shared references within nested objects.
Deep copying, on the other hand, ensures complete independence between the original and cloned objects but can be more complex and resource-intensive.
"""

import copy
from abc import ABC
from typing import Self


class Cloneable(ABC):
    def clone(self) -> Self:
        return copy.copy(self)
