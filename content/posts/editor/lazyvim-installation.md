+++
title = 'LazyVim 安装'
date = 2023-12-20T14:25:18+08:00
tags = ['lazyvim', 'nvim']
categories = 'editor'
+++

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
git clone https://github.com/LazyVim/starter ~\AppData\Local\nvim
nvim
```

将会自动完成后续一切设置，实现真正的 Lazy 。

但问题往往出现在网络上，首先是克隆仓库来自 GitHub ，经常遇到超时、重置等问题。
这里的解决方案是选择 SSH 协议或者使用镜像站，推荐使用 SSH 协议，但需要预先配置 SSH 公钥。

```
git clone git@github.com:LazyVim/starter ~\AppData\Local\nvim
```

第二步修改启动器里的链接，启动器路径： `~\AppData\Local\nvim\lua\config\lazy.lua`

```lua
-- 修改 lazy.nvim 协议为 SSH
"git@github.com:folke/lazy.nvim.git"

-- 修改插件下载协议为 SSH
git = { url_format = "git@github.com:%s.git" },
```

之后进入 neovim 即可正常启动。如果先前使用 HTTPS 启动一次失败了，要先清除缓存，
即删除 `nvim-data/lazy` 目录，然后重新启动。

另外 lsp 管理插件 mason 会遇上 GitHub release 下载链接被重置的问题，
解决办法是使用镜像或加速：修改文件
`~\AppData\Local\nvim-data\lazy\mason.nvim\lua\mason\settings.lua`
约 55 行的 `download_url_template` 为镜像站，如 `https://hub.nuaa.cf`
。

---

完