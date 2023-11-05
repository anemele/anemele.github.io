+++
title = 'rvv: Python 虚拟环境管理器'
date = 2023-10-30T01:49:33+08:00
draft = true
tags = ['rvv', 'Python', 'venv']
categories = 'computer'
+++

rvv 是一个用 Rust 实现的 Python 虚拟环境管理工具，可以实现虚拟环境的
创建、查询、移除、激活功能。

<!--more-->

# 为什么 Python 要用虚拟环境？

有人抱怨 Python 的虚拟环境完全没有必要，十分麻烦，不如 Java 等在本地设置一个中心库，
用版本号区分同名库，使用哪个版本就调用哪个版本。实际上，这是由于 Python 动态语言的特性决定的。

Python 在设计之初就确定了解释器找寻库的方式：
遍历启动解释器后设置的 `sys.path` 变量[^ref-sys-path]。
如果将所有第三方库统一放置在本地的一个中心库，解释器会陷入迷茫状态：
`import requests` 该调用哪个版本？

[^ref-sys-path]:https://docs.python.org/3/tutorial/modules.html#packages

这时有两种解决方案：
一是在源码里指明版本号，如 `import requests@2.30.0`；显然这是不能接受的；
二是参考 Java 的 `pom.xml` ，创建一个记录第三方依赖版本的清单，解释器运行前先读取清单，再从中心库找到
对应版本；不同于编译型语言可以在编译前解决依赖问题，这会大大降低解释器执行效率。

因此，Python 设计了虚拟环境，将所有依赖在一个独立环境里构建完成，保证运行前无障碍。

# 现有哪些虚拟环境方案？

- `venv`
- `virtualenv`
- `virtualenvwrapper`
- `conda`
- ...

# 为什么用 rvv ？

当前虚拟环境方案有很多，以上仅列举了最知名的几个。方案很多，然而都有各自的不尽人意。

`venv` 是标准库，随着版本一起发行，一般不能改变，而且功能较少，不够灵活。

`virtualenv` 是 Python2 时代创建的项目，延续到 Python3 ，功能强大，依赖 `venv`。
可以随时随地建立虚拟环境，可以指定 Python 版本（需要预装）。

`virtualenvwrapper` 顾名思义是 `virtualenv` 的包装器，因为 `virtualenv` 创建的环境是分散的，
包装器将这些环境集中管理。

`conda` 是 Python 发行版 `Anaconda` 的包管理工具，功能强大，集中管理。
可以指定 Python 版本（无需预装），每个虚拟环境都要独立安装解释器。
`conda` 有自己维护的源，包含了很多非 Python 的工具，如 GCC 编译器。部分与 pip 不兼容。

<!-- 各自优劣？
rvv 应运而生 -->

# rvv 设计思路

# rvv 使用方法

# 后续计划
