---
title: fedora 踩坑
date: 2024-04-11
tags:
 - fedora
 - nvim
 - libluv
categories: os
---

# neovim

fedora 安装 neovim 后无法打开，总是提示
`nvim: symbol lookup error: /lib64/libluv.so.1: undefined symbol: uv_thread_getpriority`
，最终在一个 issue 里找到了
[方法](https://github.com/neovim/neovim/issues/24992#issuecomment-1704425709)
，执行以下命令即可：

```shell
sudo dnf install libluv-1.44.2.1
```