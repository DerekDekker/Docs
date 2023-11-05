# React 基础



[HTML转JSX](https://transform.tools/html-to-jsx)
---
## 命令

```shell
# 项目创建
npx create-react-app 名称
#
npm start
```

---
## 导入

```javascript
import 组件名 from './组件文件.js';
import { 具名组件 } from './组件文件.js';
```

---
## 组件

定义组件

```javascript
function 名称() { }
```

### 默认导出组件
```javascript
export default function 名称() { }
```

### 具名导出组件
```javascript
export function 名称() { }
```

### 返回标签

```javascript
return <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />;
```

```javascript
return (
  <div>
    <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />
  </div>
);
```

---
## 语法

### 大括号使用

```javascript
<img className={avatar} src={avatar}/>

<h1>{name}'s To Do List</h1>

<h1>To Do List for {formatDate(today)}</h1>

```

### 双大括号

双大括号包裹的是对象

```javascript
<ul style={
  {
    backgroundColor: 'black',
    color: 'pink'
  }
}>
```

## 对象创建与使用

```javascript
const person = {
  name: 'Gregorio Y. Zara',
  theme: {
    backgroundColor: 'black',
    color: 'pink'
  }
};

<h1 style={person.theme}>{person.name}'s Todos</h1>
```

---
## JSX


```javascript
JSX规则 用于返回多个根元素
<></>

```

---
## 传递参数

```javascript
function Avatar({ person, size = 100 }) {
  // ...
}

<Avatar person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }} size={100} />
```

```javascript
function Avatar(props) {
  let person = props.person;
  let size = props.size;
  // ...
}

<Avatar person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }} size={100} />


```

```javascript
// 将父组件的props值全部传递给子组件
<Avatar {...props} />
```

---
## children

组件嵌套

```javascript
function Card({ children }) {
  return (
    <div>
      {children}
    </div>
  );
}

function Profile() {
  return (
    <Card>
      <Avatar />
    </Card>
  );
}
```

---
## map 列表


```javascript
const listItems = 数组.map(变量 =>
  <li>...</li> // 隐式地返回！
);

const listItems = 数组.map(变量 => { // 花括号
  return <li>...</li>;
});
```

---
## 条件渲染

```javascript
function 组件名() {
  if (条件){
    return HTML标签;
  }
  return HTML标签;
}


```

??? note "描述"

    也可以返回 null


### 三目运算符

```javascript
条件? 内容1 : 内容2
```

??? note "描述"

    条件为true时返回内容1, 条件为false时返回内容2


```javascript
条件? 内容1
```

??? note "描述"

    只有条件满足时渲染



---
## for

```javascript
for (let i = 1; i <= 12; i++) {
    // 代码
}
```

---
## switch

```javascript
switch (变量){
    case 值1:
        return HTML标签
    case 值2:
        return HTML标签
    default:
        return HTML标签
}
```

---
## onClick

```javascript
<button onClick={onClick}></button>

function onClick(e) {
    // e 是触发此函数的组件
}
```

??? note "描述"

    按钮的点击函数

---
## useState

状态

```javascript
const [person, setPerson] = useState(默认值);

// 设置新值
setIndex(值);

// 状态更改
setIndex({
  ...person,
  name: 新值
});

setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        title: 新值
      }
});
```

??? note "描述"

    设置变量名 用于设置的变量名 默认值