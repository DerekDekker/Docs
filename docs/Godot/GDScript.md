# GDScript

---
## 变量

```gds
var 变量名 = 值
var 变量名: 数据类型
# 静态变量
const 变量名 = 值

```

数据类型
```python
bool
int
float
String
null
```

---
## 语法

```gds
# 导入变量
@export var number: int = 5 

# 在外部保存节点
onready var 名称 = 节点 
```

---
## 方法

静态方法

```gds
static func 名称():
    return 值
```

---
## 引擎方法

```gds
# 添加对象作为子节点
add_child(对象)

# 获取本节点
self
$"."

# 获取父节点
get_parent()
$"../"

# 获取子节点
$子节点名称

# 获取节点
get_node("节点名称")
get_node("节点名称/节点名称")
get_node("/root/节点名称")
get_node("../节点名称")
```

---
## 类

```gds


class 名称:
    extends 父类  # 继承
    pass
    
    func _init():
        pass
    
    func 方法名():
        .父类方法()  # 会执行父类被重写的方法 
```

---
## 优化

```gds
# 释放对象 优化内存 
对象.free()
# 释放对象 优化内存 这一帧结束时去释放 效率更高
对象.queue_free()
# 释放对象 优化内存
对象.unreference() 
```

---
## 节点

### Sprite

```gds
# 设置图片
var icon = preload("res: //icon.png")
对象.set_texture(icon)
```