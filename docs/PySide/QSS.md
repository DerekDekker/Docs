# QSS


---
## 组件样式

```python
控件.setStyleSheet('background-color:#778877;')
```

### 组件样式

```python
qssStyle = '''
    选择器{
        background-color: #881144
    }
'''

主窗体.setStyleSheet(qssStyle)
```

### 设置QSS文件

```python
# 设置QSS文件
with open("qss/style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)

主窗体.setStyleSheet(qssStyle)
```

---
## 样式

```qss
# 颜色
color: #ffee00;

# 背景颜色
background-color: #881144;

# 背景渐变
background: qlineargradient(x1: 0.3, y1: 0, x2: 1, y2: 0, stop: 0 #00ffec, stop: 1 #f9ff00);

# 背景图片 整张
border-image:url(img/img.jpg);

# 背景图片
background:#000 url(01.gif) no-repeat 位置;

# 字体大小
font-size:60px; 

# 字体样式
font-family: "Unifont";

# 宽
width:100px;

# 高
height:100px;

# 取消边框
border: none;

# 边框 可选方向
border: 1px solid #21262d;

# 边框
border:10px solid red;

# 内边距
padding:10px 5px;

# 外边距
margin:10px;

# 边缘
border-radius: 4px;

# 字体边据
letter-spacing:10px;

```

---
## 选择器

```
*          		匹配所有控件

控件     		类型选择器

控件[name='myBtn'] 属性选择器

#名称		ID选择器

控件1, 控件2 	多个选择器

:hover		鼠标悬停样式

:pressed		鼠标按下时

:active		所指元素处于激活状态
```

### 选择器使用

```
属性
控件.setProperty('name', '名称')

ID
控件.setObjectName('名称')
```