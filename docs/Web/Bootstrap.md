# Bootstrap


---
## 基础

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
<!--      移动端响应式-->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
  </body>
</html>

```

---
## 修饰

`text-center`  内容剧中

`p-4`  内边距

`px-4`  内边距 左右

`py-4`  内边距 上下


`g-5`  外边距

`gx-5`  外边距 左右

`gy-5`  外边距 上下

`g-0`  外边距 取消


---
## 布局

### container

响应式布局

```html
<div class="container">
  <!-- Content here -->
</div>
```

---
## 嵌套布局

### row

行

!!! note ""
    一个row能容纳下12个col-1列

`row`  

修饰

`justify-content-屏幕大小-center`  剧中

`row-cols-2`  一行能存放下多少个col, 多出来的自动换行

`row-cols-auto` col的宽度将根据内容宽度来决定

`row-cols-1 row-cols-sm-2 row-cols-md-4`  根据屏幕来决定能放几个



### col

列

`col`

`col-1` 到 `col-9` 占用几个列的空间

`col-屏幕大小-auto`  它的宽度将根据内容宽度来决定

`col-屏幕大小-2`  符合屏幕大小后 它占两个列的空间, 否则占用整个空间

`col-屏幕大小`  符合屏幕大小后 拥有col特型, 否则占用整个空间

#### 演示

`col-6 col-屏幕大小-4`  满足屏幕大小后占用4列空间 否则占用6列大小


---
## 参考


| 屏幕大小 | 大小     |
|------|--------| 
| xs   | <576px | 
| sm   | ≥576px   |
| md   | ≥768px   |
| lg   | ≥992px   |
| xl   | ≥1200px   |
| xxl  | ≥1400px   |



























