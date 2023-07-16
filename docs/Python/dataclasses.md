# dataclasses

---
## 基础

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    occupation: str

    def greet(self):
        print(f"Hello, my name is {self.name}!")

# 创建一个Person对象
person = Person("Alice", 25, "Engineer")

# 调用自定义的方法
person.greet()  # 输出: Hello, my name is Alice!

```

## 不可以修改

通过使用frozen=True参数 数据类设置为不可变的.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

person = Person("Alice", 25)

# 尝试修改属性的值将引发异常
person.age = 26  # 引发dataclasses.FrozenInstanceError异常
```

## 继承

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    department: str

employee = Employee("Alice", 25, "Engineering")

print(employee.name)  # 输出: Alice
print(employee.department)  # 输出: Engineering

```

## field

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = field(default=0,)  # 默认值
    age: int = field(default_factory=函数)  # 默认值工程 通过一个函数的返回值作为默认值
    age: int = field(init=True)  # 是否在创建对象时初始化值
```

## 换字典

```python
from dataclasses import dataclass, asdict

person_dict = asdict(dataclass实例)

```