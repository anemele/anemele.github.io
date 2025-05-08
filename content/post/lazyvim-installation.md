---
title: LazyVim 安装
date: 2023-12-20
lastmod: 2025-05-08T11:14:12+08:00
tags:
 - LazyVim
 - nvim
categories: editor
---

LazyVim 是基于 lazy.nvim 的一个 neovim 发行版，类似于预先安装很多插件的 vscode
，实现了即开即用。

<!--more-->

LazyVim 的安装很方便，参考[官方教程](https://www.lazyvim.org/installation)，
只需克隆一份[启动器](https://github.com/LazyVim/starter)，
然后进入 neovim 就会自动下载相关插件，插件下载完毕即是完成。

Windows 路径为 `~\AppData\Local\nvim` ， Linux/macOS 路径为 `~/.config/nvim` 。
首先备份设置和数据，即 `nvim` 和 `nvim-data` 两个目录，然后将
[启动器](https://github.com/LazyVim/starter)
克隆到 `nvim` 目录。如果网络顺畅，直接进入 neovim

```
git clone https://github.com/LazyVim/starter ~/.config/nvim
nvim
```

将会自动完成后续一切设置，实现真正的 Lazy 。

## 网络问题

问题往往出现在网络上，首先是克隆仓库来自 GitHub ，经常遇到超时、重置等问题。
这里的解决方案是选择 SSH 协议或者使用镜像站，推荐使用 SSH 协议，但需要预先配置 SSH 公钥。

> 先前修改 LazyVim 配置的方法不再推荐。

git config 有一个选项 `url.xxx` 可以将 https 协议的地址替换为 ssh 协议的地址。

```
[url "git@github.com:"]
        insteadof = https://github.com/
```

写入配置之后从头开始安装 LazyVim 即可。如果先前使用 HTTPS 启动一次失败了，要先清除缓存，
即删除 `nvim-data/lazy` 目录，然后重新启动。

## mason 插件

另外 mason 插件会遇上 GitHub release 下载链接被重置的问题，解决办法是使用镜像。
在 `nvim/lua/config/lazy.lua` 后加上

```lua
require("mason").setup({
  github = {
    -- 此处为镜像链接
    download_url_template = "https://github.com/%s/releases/download/%s/%s",
  }
})
```

镜像链接多不稳定，以下列出几个作为参考：

```text
https://hub.nuaa.cf/%s/releases/download/%s/%s
https://hub.yzuu.cf/%s/releases/download/%s/%s
https://dgithub.xyz/%s/releases/download/%s/%s
https://mirror.ghproxy.com/https://github.com/%s/releases/download/%s/%s

