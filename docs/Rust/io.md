# io

`use std::io;`


---
## 基础

```rust
io::stdin()
    .read_line(&mut guess)
    .expect("Failed to read line");
```