# React Native 组件

---
## 基本

### Text

```js
<Text>内容</Text>
```

### Button

按钮

```js
<Button
    title='标题'
    onPress={函数}
    color={"red"}
/>
```

### Switch

开关

```js

<Switch 
  trackColor={{true:'red', false: "blue"}}  // 状态的样式
  value={true}  // 状态
  onValueChange={}  // 点击事件
/>

```

### SafeAreaView

安全区域视图

```js
<SafeAreaView>
</SafeAreaView>
```

### StatusBar

状态栏

```js
<StatusBar
  hidden={false} // 隐藏
  backgroundColor={"blue"}  // 样式 只有在安卓下有效
/>
```  

### 加载等待

```js
<ActivityIndicator 
  color="red"
  size={"large"}
/>
```

### 图片

```js
<Image
  style={{ width: 100, height: 100 }}
  // source={require('./src/images/01.jpg')}
  source={{ uri: 'https://facebook.github.io/react-native/img/tiny_logo.png' }}
/>
```

### TextInput

输入框

```js

<TextInput 
  style={{width:100, height: 20, borderWidth:1}}
  placeholder='请输入'  // 提示
  value='123'  // 值
  onChangeText={(val)=>{console.log(val)}}  // 文本改变触发函数
  secureTextEntry={false}  // 是否为密码框
  keyboardType='number-pad'  // 键盘类型
/>


```