# React 基础



[官方文档](https://zh-hans.react.dev/learn)

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
    // e 是触发此事件函数的组件
}
```

```javascript
<button onClick={() => {
  onClick(值)
}}></button>
```

```javascript
<button onClick={e => onClick(值)}></button>

```

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

setIndex({
      ...person,
      artwork: {
        ...person.artwork,
        title: 新值
      }
});

// 在下次渲染前多次更新同一个 state
setIndex(变量 => 值);
```

??? note "描述"

    设置变量名 用于设置的变量名 默认值


??? note "更新 state 中的对象"

    state 中可以保存任意类型的 JavaScript 值，包括对象。但是，你不应该直接修改存放在 React state 中的对象。相反，当你想要更新一个对象时，你需要创建一个新的对象（或者将其拷贝一份），然后将 state 更新为此对象。

```javascript
// 属性的动态命名
 function handleChange(e) {
    setPerson({
      ...person,
      [e.target.name]: e.target.value
    });
}


```

### 筛选

```javascript
setArtists(
  数组.filter(a => a.id !== artist.id)
);
```

### 强制重置组件

只需要给组件key赋予 状态 值 当状态改变时组件也会跟着重置

```javascript
<组件 key={状态.值}/>
```

---
## Context

```javascript
// 定义
const LevelContext = createContext(0);

// 获取
const level = useContext(LevelContext);
```

??? note "描述"

    定义的对象名称大写

    可以单独在一个文件内定义


```javascript
// 子组件获取 Context对象 值时会获取上层最近组件传递的值

<Context对象.Provider value={值}>
    子组件
</Context对象.Provider>
```

---
## 事件

事件命名都是以handle开头

```javascript
<button onClick={function handleClick() {
  alert('你点击了我！');
}}>

<button onClick={() => {
  alert('你点击了我！');
}}>
```

### 阻止事件传播

在子组件触发的事件函数中运行, 

```javascript
e.stopPropagation();
```

??? note "描述"

    阻止因点击子组件而触发父组件的事件行为


阻止浏览器默认行为

```javascript
e.preventDefault();
```

















