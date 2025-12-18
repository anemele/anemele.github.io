---
title: Gitee 添加 ssh 公钥
date: 2023-11-22
tags:
 - ssh
 - git
 - gitee
categories: computer
---

先前一直使用 GitHub ，已经添加了两个 ssh 密钥，在
`~/.ssh` 目录下有 6 个文件：

- config
- id_rsa
- id_rsa.pub
- id_rsa_163
- id_rsa_163.pub
- known_hosts

因为 GFW 的存在， GitHub 访问速度很慢。现在急需使用 git 服务器，于是启动了 Gitee 。

创建账号等准备工作完成后，就要添加 ssh 公钥了。

按部就班，使用 ssh 工具生成密钥对

```bash
ssh-keygen -t rsa -C "your_name@example.com"
# 有三步输入，第一步可以设置密钥对名字（默认 id_rsa），其余两步可以跳过。

cat ~/.ssh/id_rsa_gitee.pub
# 复制公钥内容到 Gitee
```

然后创建私有仓库，与本地仓库关联。在 pull/push 的时候提示无权限。
查阅很多博客，然并卵。

无意间想到 config 文件可能有玄机，打开一看，果然是 GitHub 的密钥配置。
按照格式，添加 Gitee 的配置，再次 pull/push 果然成功。

配置如下（用户目录是完整路径，这里改为 `~`）

```text
Host github.com
User git
HostName ssh.github.com
Port 22
IdentityFile ~/.ssh/id_rsa

Host gitee.com
User git
HostName gitee.com
Port 22
IdentityFile ~/.ssh/id_rsa_gitee
```
