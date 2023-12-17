+++
title = 'Python 项目管理'
date = 2023-06-22T22:19:12+08:00
lastmod = 2023-11-05T22:22:22+08:00
draft = false
tags = ['Python']
categories = 'computer'
+++


最近迷上了各自编程语言的项目管理，才发现以前的编程方式是多么简陋，放着这么多先进工具不使用，反而手动处理各自问题。

项目管理主要就是管理项目的各种依赖，也可以称为包管理。现在的包管理大都趋同，向着一个更方便更合理的方向发展。


<!--more-->


# 项目管理文件

Python 早期是 `pip virtualenv pipreqs requirements` 组合，现在有了某 PEP 提出的 `pyproject.toml` ，并且得到很多支持。pypa 的 pip 对此支持还不够好，推荐使用 poetry ，有点类似 yarn 之于 npm 。

> Nodejs 有 package.json 和 yarn 。
>
> Java 有 pom.xml 和 maven ，以及 build.gradle 和 gradle 。
>
> Go 有 go.mod 。
>
> Rust 有 Cargo.toml 和 cargo 。
>
> 期待 C++ 早日推出好用的包管理工具。

*231105 补充： C++ 有一个 xmake 也很好用*

# 依赖版本规则

包管理的依赖一般使用语义版本（semantic version, semver）格式，即版本号由 `major.minor.micro` 组成。为方便说明，以下使用 `x.y.z` 。

项目依赖一般写作
`abc = "x.y.z"`
的形式，表示依赖 x.y.z 这个版本的 abc 。

有些情况写作 `"~x.y.z"` 或者 `"^x.y.z"` ，还有写 "latest" 的情况。
这些写法表示依赖的版本可以变化：
- 只有 x.y.z 的写法表示指定该版本，不允许变动。
- 以波浪线 `~` 开头的写法表示将 z 升级到最新版本，但 x y 保持不变。
- 以上箭头 `^` 开头的写法表示将 y.z 升级到最新版本，但 x 保持不变。
- latest 顾名思义就是最新版。

用不等式表示波浪线和上箭头的语义：

```text
~x.y.z
x.y.z <= version < x.(y+1).0

^x.y.z
x.y.z <= version < (x+1).0.0
```

以上存在一种例外情况：

当依赖处于开发之中，即 x 为 0 ，需要后移一位。
例如 ^0.9.3 表示 0.9.3 <= version < 0.10.0 ， ~0.9.3 等价于 0.9.3 。
如果 x 和 y 都为 0 则需要再后移一位。当然，这种情况一般不会发生。
