# Nmap

---
## 基础

```shell
# 探索 列出开放端口
nmap google.com 
```

??? note "参数"

    `—dns-servers 8.8.8.8` # 指定DNS服务器

    `-Pn google.com` # 停止ICMP请求防止触发防火墙

    `-p 1-1000` # 指定端口范围 也可以是固定端口