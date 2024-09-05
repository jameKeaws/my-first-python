# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, anothervalue):
        self.value2 = anothervalue
        

obj = ImmutableClass()
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another String"
# print(obj.value1, obj.value2)

# TODO: even functions within the class can't change anything
# obj.some_func(20)
# print(obj.value1, obj.value2)

# Allowed to change value at construction time

obj2 = ImmutableClass("Another String", 54)
print(f"Object 2 {obj2.value1} {obj2.value2}")
obj2.some_func(23)
print(obj2.value1, obj2.value2)
