# Rich基础

[文档](https://rich.readthedocs.io/en/latest/index.html)

[颜色](https://rich.readthedocs.io/en/latest/appendix/colors.html)


---
## 基础

```python
from rich.console import Console

console = Console()
```

---
## 输出

```python
# 打印
console.print(":1st_place_medal:")
# 日记
console.log("Hello, World!")
# json
console.print_json('[false, true, null, "foo"]')
```

---
## 标记

```python
print("[bold red]Hi[/] Hello")
print("Visit my [link=https://www.google.com]blog[/link]!")
```

---
## style

style 是 Console与print的属性

`white on blue`  文字与背景颜色

`bold`或`b` 粗体

`blink` 闪烁

`reverse`或`r` 前景和背景颜色反转

`underline`或`u` 下划线

`strike` 或 `s` 删除线

---
## 布局

```python
overflow="fold"  # 换行
overflow="crop"  # 多出不显示
overflow="ellipsis"  # 多出省略号
```

```python
justify="left"  # 方向
width=12  # 宽度
```

### Layout

```python
from rich.layout import Layout

layout = Layout()

# 上线布局
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

# 左右布局
layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

# 添加布局
layout["right"].split(
    Panel("World!"),
    Panel("World!")
)

# 更新布局
layout["left"].update(
    Layout(Panel("Hello")),
)
```

`print(layout.tree)`  打印布局结果

`layout["left"].size =10` 大小 也可以None为取消限制

`layout["left"].ratio=2`  弹性2各

`layout["lower"].minimum_size=10`  最小大小

`layout["upper"].visible=False`  最大大小


---
## 组件

### 分割线

```python
console.rule("[bold red]名称")
```

### 边框
```python
from rich.panel import Panel

Panel("内容")
```
`title="标题"`  # 标题

`title_align="left"`  # 标题方向

`subtitle="副标题"`  # 副标题

`subtitle_align="right"`  # 副标题方向

`expand=True`  # 是否扩展

`padding=1` 或 `padding=(1,2)`  # 内边距

```python
from rich.console import Group

# 分组
panel_group = Group(
    Panel("Hello", style="on blue"),
    Panel("World", style="on red"),
)
```

### 进度条

```python
from rich.progress import track

for i in track(range(20), description="Processing..."):
    print(i)
    time.sleep(1)  # Simulate work being done
```

```python
from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.001)
```
            
### 表格

[边框颜色风格](https://rich.readthedocs.io/en/latest/appendix/box.html)

```python
from rich.console import Console
from rich.table import Table, Column
from rich import box

table = Table(title="我的完美表格")
```

`box=box.ASCII2`  边框颜色风格 

`show_header=True` 是否 显示头

`expand=False`  是否 适应宽度

`show_lines=False` 是否 显示行之间的线条

`show_footer=False` 是否 显示页脚

`padding=1` 或 `padding=(1,2)` 内边距

`style="#003C43"` 适用于整个桌子的样式

`border_style="red"` 边框颜色

`row_styles=["red", "blue", "#003C43"]` 行与行的内容循环显示颜色

`header_style="red"` 头部标题样式

`title_style="red"` title标题样式

`footer_style=""` 页脚样式

`caption="标题"`  页脚标题

`caption_style="red"` 页脚标题样式


`highlight=False` 是否 启动自动高亮显示


```python
# 表格头部
table.add_column("标题", style="cyan",  header_style="red")
```

`justify="right"` 方向

`width=50`  宽度

`min_width=50`  最小宽度

`max_width=50`  最大宽度

`style="red"`  列颜色

`header_style="red"`  标题颜色

```python
# 行数据
table.add_row("内容1", "内容2", "内容3")
```

持续更新表格

```python
import time

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
    for row in range(12):
        time.sleep(0.4)  # arbitrary delay
        # update the renderable internally
        table.add_row(f"{row}", f"description {row}", "[red]ERROR")
```

---
## 功能


```python
# 等待执行完成
with console.status("Monkeying around...", spinner="aesthetic"):
    time.sleep(1)
```

```python
# 全凭阅读 按q退出
with console.pager():
    console.print("内容")
```

```python
# 全凭阅读 等待执行完成退出
with console.screen():
    console.print("内容")
    time.sleep(2)

```

---
## 颜色

```python
console.print("Hello", style="magenta")
console.print("Hello", style="color(6)")
console.print("Hello", style="#ab3a3a")
console.print("Hello", style="rgb(175,50,175)")
```

---
## 输入

```python
# 输入
console.input("内容")
```

```python
from rich.prompt import Prompt
name = Prompt.ask("请输入")

name = Prompt.ask("请输入", default="默认值")

# 不在选项内不被接受 并需要重新输入
name = Prompt.ask("请输入", choices=["选项", "选项", "选项"], default="默认值")
```

```python
from rich.prompt import Confirm

is_rich_great = Confirm.ask("是否确认?",)
```

`password=True`  密码

---
## emoji

符号

`python -m rich.emoji`


---
## 扩展

### Markdown

```python
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)
```

### 代码渲染

[主体](https://pygments.org/demo/)

```python
from rich.console import Console
from rich.syntax import Syntax

console = Console()
syntax = Syntax.from_path("test.py", line_numbers=True, theme="vim")
console.print(syntax)
```

`background_color="#ff0000"`  背景颜色