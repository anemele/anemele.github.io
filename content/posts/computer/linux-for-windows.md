+++
title = 'Linux for Windows'
date = 2022-07-21T09:42:11+08:00
draft = false
tags = ['Linux', 'Windows']
categories = 'computer'
+++

Linux 是开发的理想环境，但在办公娱乐不如 Windows。

<!--more-->

为方便在 Windows 下开发，需要搭建 Linux 环境，目前已知的方案包括：

- 虚拟机
  - virtual box
  - vmware
- wsl
- msys
- Cygwin

虚拟机与 wsl 都提供了完整的 Linux 系统环境，而 msys 和 Cygwin 只是模拟了 Linux 部分环境。

虚拟机使用 vbox + Linux 镜像，做开发不必要图形界面，安装 server 版本即可。
wsl 与虚拟机类似。
做简单开发，使用 msys + mingw 即可，约占用硬盘 700 MB 。
Cygwin 过时了。

**MSYS + MinGW 环境配置**

1. 安装 MinGW 与 MSYS2
   1. MinGW 可以从 sourceforge 下载 8.1，也可以从 github 下载更新版本
   2. MSYS2 可以从清华镜像站下载，也可以从 github 下载
2. 配置环境变量
   1. `%MINGW%\bin`
   2. `系统变量 -> MSYS2\PATH\TYPE\:inherit`
3.  注册表添加“在此处打开 MSYS”
   1. 注册表路径： `HKEY\CLASSES\ROOT\Directory\Background\shell` 新建项 MSYS，设置默认值为 “在此处打开 MSYS”
   2. 新建字符串项 Icon，设置路径为 `%MSYS%\msys2.ico`
   3. MSYS 新建子项 command，设置默认值为 `%MSYS%\msys2\shell.cmd -here`
