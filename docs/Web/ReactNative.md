# ReactNative 基础



``` npx react-native@latest init Awesome ``` 安装项目


## 快速创建代码段落


`rnc`  类组件

`rncs`  带样式

---
## 函数

```js
函数名 = () => {}
```

---
## 常用函数

`console.log("内容")`  打印内容

### 弹窗

```js

Alert.alert(
    "标题",
    "内容",
    [
        {
            text:"标题",
            onPress:() => {},
            style:"cancel"
        },
        {
            text:"标题",
            onPress:() => {},
            style:"cancel"
        },
    ]
);
```