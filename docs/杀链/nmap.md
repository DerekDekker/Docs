# Nmap

会显示目标服务器开放的端口服务与IP地址

---
## 基础

```shell
# 探索 列出开放端口 服务 IP地址
nmap google.com 
```

??? note "参数"

    `—dns-servers 8.8.8.8` # 指定DNS服务器

    `-Pn google.com` # 停止ICMP请求防止触发防火墙

    `-p 1-1000` # 指定端口范围 也可以是固定端口

    `-v` # 持续输出 不需要等待一次性输出结果

    `-oX test.xml` # 保存为xml


```shell
# 服务指纹探测 列出服务详情 版本信息
nmap -sV google.com
```

```shell
# 侵略性探测
nmap -A google.com
```



---
## 主机发现

```shell
# ping 扫描 TCP SYN 扫描 
nmap -sP 192.168.1.1/24

# ping 扫描
nmap -sn 192.168.1.1/24
```

