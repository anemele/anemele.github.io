---
title: LazyVim 安装
date: 2023-12-20
lastmod: 2025-11-20T20:32:36+08:00
tags:
 - LazyVim
 - nvim
 - neovim
categories: editor
---

LazyVim 是一个 neovim 发行版，类似于预先安装很多插件的 vscode，实现了即开即用。

<!--more-->

LazyVim 的安装很方便，参考[官方教程](https://www.lazyvim.org/installation)，
只需克隆一份[启动器](https://github.com/LazyVim/starter)，
然后进入 neovim 就会自动下载相关插件，插件下载完毕即是完成。

如果是第一次使用 neovim，直接克隆并启动即可。
配置（启动器）路径：Windows 为 `~\AppData\Local\nvim` ， Linux/macOS 为 `~/.config/nvim` 。

如果是以前使用过 neovim，建议先备份配置和数据，即
`~\AppData\Local\nvim` 和 `~\AppData\Local\nvim-data` 两个目录，
Linux/macOS 为 `~/.config/nvim` 和 `~/.local/shared/nvim` 。

```
git clone https://github.com/LazyVim/starter ~/.config/nvim
nvim
```

如果网络顺畅，直接进入 neovim 将会自动完成后续一切设置，非常 Lazy 。

## LazyVim 启动

问题往往出现在网络上，首先是克隆仓库来自 GitHub ，经常遇到超时、重置等问题。
这里的解决方案是选择 SSH 协议或者使用镜像站，推荐使用 SSH 协议，但需要预先配置 SSH 公钥。
然后改用

```
git clone git@github.com:LazyVim/starter ~/.config/nvim
```

之后编辑 `nvim/lua/config/lazy.lua`

```lua
-- 修改一处
-- local lazyrepo = "https://github.com/folke/lazy.nvim.git"
local lazyrepo = "git@github.com:folke/lazy.nvim.git"

-- 添加一处
require("lazy").setup({
  -- use git protocol
  git = { url_format = "git@github.com:%s.git" },
  -- ...
})

```

写入配置之后从头开始安装 LazyVim 即可。

## mason 插件

mason 插件通常来自 GitHub release ，经常遇到网络问题，解决办法是使用镜像。

创建 `nvim/lua/plugins/mason.lua` （文件名任意）并写入

```lua
return {
  {
    "mason-org/mason.nvim",
    opts = {
      github = {
        download_url_template = "https://edgeone.gh-proxy.com/github.com/%s/releases/download/%s/%s",
      },
    },
  },
}
```

## 结语

最后补充说明，每个人的配置都是独一无二的。当你逐渐资深，你会发现通用配置已经无法满足需求，必须自主定制。

LazyVim 启动器克隆完成后有一个操作是删除 git 仓库，这便是为了避免后续操作影响到启动器的配置。
所以不要完全依赖 LazyVim 已有的配置，要有个性。