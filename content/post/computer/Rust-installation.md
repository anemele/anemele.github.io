+++
title = 'Rust 编程语言安装教程'
date = 2024-01-20T22:49:16+08:00
tags = ['Rust']
categories = 'computer'
+++

[Rust](https://www.rust-lang.org/) 是一门可靠而高效的编程语言，其安装也很简便。

Windows 用户只需下载启动器
[rustup](https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe)
运行即可。

为了方便下载，在运行启动器之前先设置两个环境变量（**建议设置为永久环境变量**），
使用国内镜像加速：

以 Windows 为例

```bat
set RUSTUP_DIST_SERVER=https://rsproxy.cn
set RUSTUP_UPDATE_ROOT=https://rsproxy.cn/rustup
@REM 永久环境变量
setx RUSTUP_DIST_SERVER https://rsproxy.cn
setx RUSTUP_UPDATE_ROOT https://rsproxy.cn/rustup
```

或者

```bat
set RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
set RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
@REM 永久环境变量
setx RUSTUP_DIST_SERVER https://mirrors.ustc.edu.cn/rust-static
setx RUSTUP_UPDATE_ROOT https://mirrors.ustc.edu.cn/rust-static/rustup
```

设置好环境变量，运行启动器（一般选择默认配置），在网络良好的情况下很快就完成 Rust 的安装。

然后在 .cargo 目录下编写配置文件，方便后续包管理。

```toml
# ~/.cargo/config

[source.crates-io]
replace-with = 'rsproxy-sparse'
[source.rsproxy]
registry = "https://rsproxy.cn/crates.io-index"
[source.rsproxy-sparse]
registry = "sparse+https://rsproxy.cn/index/"
[registries.rsproxy]
index = "https://rsproxy.cn/crates.io-index"
[net]
git-fetch-with-cli = true
```

在 Windows 平台安装并选择 MSVC 工具链时，需要下载
[MSVC Build Tools（Microsoft C++ 生成工具 - Visual Studio）](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/)，
安装 C++ Desktop Development ，其中**必选的两项**是 `MSVC vxxx 生成工具` 和 `Windows SDK` ，根据自己的平台选择。