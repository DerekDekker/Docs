# UI


---
## 基础

```javascript
"ui";
ui.layout(
    // 布局
    <vertical>
        <button text="第一个按钮"/>
        <button text="第二个按钮"/>
    </vertical>
);
```

---
## 布局

```javascript
// 垂直
<vertical></vertical>

// 水平
<horizontal></horizontal>
```





---
## 控件

```javascript
// 按钮
<button text="按钮"/>
```

```javascript
// 文本
<text text="文本" />
```

`line="3"`  文本行数

`maxLines="3"`  文本行数


```javascript
// 输入框
<input text="输入框" />
```

`hint="提示文本"`  提示文本

`inputType="textPassword"`  文本类型  [链接](http://doc.autoxjs.com/#/ui?id=inputtype)


```javascript
// 图片
<img src="https://www.google.com/img/bd_logo1.png" />
```

`src="https://www.google.com/img/bd_logo1.png"`  网络图片

`src="file:///sdcard/1.png"`  本地图片

`scaleType="center"`  缩放模式  [链接](http://doc.autoxjs.com/#/ui?id=scaletype)


**[更多控件](http://doc.autoxjs.com/#/ui?id=勾选框控件-checkbox)**


### 属性

`id="ok"`  ID

`textSize="20sp"`  字体大小

`textColor="red"`  文本颜色

`w="100"`  宽度  `*`宽度尽量填满父布局  `auto`自适应宽度

`h="100"`  高度  `*`高度尽量填满父布局  `auto`自适应宽度

`layout_weight="1"`  控件在布局内的站位比例

`gravity="center"`  重力 [链接](http://doc.autoxjs.com/#/ui?id=gravity)

`layout_gravity="center"`  在布局中的重力

`margin="100"`  外边距  [链接](http://doc.autoxjs.com/#/ui?id=margin)

`padding="100"`  内边距  [链接](http://doc.autoxjs.com/#/ui?id=padding)


---
## 通用属性

`bg="#ff0000"`  背景颜色

`bg="file:///sdcard/1.png"`  背景图片

`alpha="0.5"`  透明度

`visibility="visible"`  可见性  [链接](http://doc.autoxjs.com/#/ui?id=visibility)