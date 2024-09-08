# 包和crate




`cargo new my-project`  创建包


---
## 基础

一个包中至多 只能 包含一个库 crate（library crate）；包中可以包含任意多个二进制 crate（binary crate）；包中至少包含一个 crate，无论是库的还是二进制的。


```

my-project/
├── Cargo.toml
│── src/
│   ├── lib.rs          # 库crate入口
│   └── main.rs         # 二进制crate入口
├── my_lib/             # 新的库 crate 的目录
│   ├── Cargo.toml      # my_lib 子库的配置文件
│   └── src/
│       ├── lib.rs      # my_lib 子库的入口文件
│       ├── module1.rs  # 子库的一个模块
│       ├── module2.rs  # 子库的另一个模块
│       └── bin/        # 二进制 crate 目录
│           ├── get_file.rs # 二进制 crate 的入口文件
│           └── other_binary.rs # 另一个二进制 crate 的入口文件


```


`main.rs` 主应用程序的入口，调用 lib.rs 中的功能。

`lib.rs` 定义公共逻辑和API，是代码复用的核心。

`bin/`  目录中的文件：定义额外的二进制crate，可以调用 lib.rs 中的功能，提供不同的应用程序入口。


`cargo run --bin cli`  运行 bin 下的 cli 二进制crate


