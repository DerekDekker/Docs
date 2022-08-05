# open

文件读取

读取 文本 图片 视频 歌曲 二进制文件


---

## 文件

```python
# 打开
名称 = open(r"路径",打开方式,encoding="编码")
```

!!! note "备注"

    编码可以不写默认ANSI


    打开方式
    
    r	读
    
    w	写，覆盖原有内容
    
    a	写，在后面增加
    
    b	二进制方式打开



---
## 方法

`变量.read(参数)`         读取文件内容，参数表示读取个数

`变量.readline()`        每次读取一行

`变量.readlines()`       读取每行，输出一个列表

`变量.write()`              写入

`变量.writelines()`     可以把列表写入

`变量.seek(0)`              光标返回开始位置

`变量.close()`              关闭文件连接

`变量.flush()`              保存，缓冲区的内容写入磁盘