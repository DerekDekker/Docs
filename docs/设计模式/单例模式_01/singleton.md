# 单列模式

继承 单列基类 的类多个实例都会是相同的实例

---
## 单列基类

```python
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```

---
## 应用

```python
class MyClass(Singleton):
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

