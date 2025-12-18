---
title: Julia 编程语言安装教程
date: 2023-12-26
tags:
 - Julia
 - installation
categories: computer
---

[Julia](https://julialang.org/) 是一门新生的科学计算编程语言，拥有动态语言的方便与静态语言的性能。

安装 Julia 推荐使用包管理器 [juliaup](https://github.com/JuliaLang/juliaup/releases/latest) ，
并按照以下几个步骤配置镜像。

1. 下载 juliaup 程序，解压并将路径放置在 PATH
2. 设置 mirror ，即设置环境变量 `JULIAUP_SERVER` [^juliaup-mirror]
3. 使用 juliaup 安装 Julia
4. 配置 Julia 镜像

juliaup mirror 可以参考 [jill](https://github.com/johnnychen94/jill.py/blob/master/jill/config/sources.json)，
可以设置永久变量，也可以设置临时变量，例如

```bash
# *nix
export JULIAUP_SERVER=https://mirrors.nju.edu.cn/julia-releases
```

```batch
@REM Windows
set JULIAUP_SERVER=https://mirrors.nju.edu.cn/julia-releases
```

Julia 包镜像

```julia
# ~/.julia/config/startup.jl
ENV["JULIA_PKG_SERVER"] = "https://mirrors.nju.edu.cn/julia"
```

[^juliaup-mirror]: https://github.com/JuliaLang/juliaup?tab=readme-ov-file#juliaup-server
