# 单列模式


- 让你能够保证一个类只有一个实例
- 为该实例提供一个全局访问节点
- 允许在程序的任何地方访问特定对象

!!! note "" 

    如果你创建了一个对象， 同时过一会儿后你决定再创建一个新对象， 此时你会获得之前已创建的对象， 而不是一个新对象。

---
## 单列基类

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
```

---
## 应用

```python
class MyClass(metaclass=SingletonMeta):
    def __init__(self, a):
        self.a = a
```

---
# 实例化

```python
a = MyClass(10)
b = MyClass(11)

b.a = 1

print(a.a)
print(b.a)
```

