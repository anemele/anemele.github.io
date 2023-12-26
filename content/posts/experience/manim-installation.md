+++
title = 'manim 安装'
date = 2023-06-14T22:46:35+08:00
tags = ['manim', 'Python']
categories = 'computer'
+++


manim 是 3blue1brown 绘制数学动画使用的 Python 库。
在安装 manim 和配置环境时遇到一大堆坑。


<!--more-->



首先是 manim 版本很多，这里的版本不是版本号，而是类似 Linux 发行版的版本。
网上的教程很多，但很少讲明它们使用的哪个版本，导致冲突混乱。
例如我已经安装了 manim `pip install manim`， 按照教程的案例，有一个 `from manimlib.imports import *` ，找不到 manimlib ， 于是 `pip install manimlib` ，谁知道它和 manim 是两个版本，而且二者冲突，导致各种报错，包括找不到 Scene、所有模块应该是 VMobject、找不到定义等一大堆。

后来两个都卸载，重装 manim 解决。

第二个问题是 manim 不稳定，目前是 0.17 版本，更新频繁，很多以前的代码要修改。

---

在 Grant Sanderson 个人仓库 [3b1b/manim](https://github.com/3b1b/manim) 的 readme 里看到了几个版本，他个人维护的版本在 pypi 的库名为 manimgl ，而社区维护的版本是 manim ，所以上面安装的实际上是社区版。
还有一个不知道谁在维护的 manimlib 。

3b1b 个人维护版本更新太慢了，推荐使用社区版。

社区版有一个[各版本说明文档](https://docs.manim.community/en/stable/faq/installation.html)。
