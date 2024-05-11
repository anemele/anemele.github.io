---
title: LazyVim 安装
date: 2023-12-20
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

但问题往往出现在网络上，首先是克隆仓库来自 GitHub ，经常遇到超时、重置等问题。
这里的解决方案是选择 SSH 协议或者使用镜像站，推荐使用 SSH 协议，但需要预先配置 SSH 公钥。

```
git clone git@github.com:LazyVim/starter ~/.config/nvim
```

第二步修改启动器里的链接，启动器路径： `nvim/lua/config/lazy.lua`

```lua
-- 修改 lazy.nvim 仓库链接协议为 SSH
-- vim.fn.system({ "git", "clone", "--filter=blob:none", "git@github.com:folke/lazy.nvim.git", "--branch=stable", lazypath })
"git@github.com:folke/lazy.nvim.git"

-- 修改插件下载协议为 SSH
-- require("lazy").setup({
git = { url_format = "git@github.com:%s.git" },
-- spec = {
-- ...
```

之后进入 neovim 即可正常启动。如果先前使用 HTTPS 启动一次失败了，要先清除缓存，
即删除 `nvim-data/lazy` 目录，然后重新启动。

另外 mason 插件会遇上 GitHub release 下载链接被重置的问题，解决办法是使用镜像。
在 `nvim/lua/config/lazy.lua` 后加上

```lua
require("mason").setup({
  github = {
    download_url_template = "https://hub.nuaa.cf/%s/releases/download/%s/%s",
  }
})
```
