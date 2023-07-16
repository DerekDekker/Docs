from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

person = Person("Alice", 25)

# 尝试修改属性的值将引发异常
person.age = 26  # 引发dataclasses.FrozenInstanceError异常
