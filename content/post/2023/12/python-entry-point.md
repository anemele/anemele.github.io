---
title: Python 脚本入口
date: 2023-12-20
lastmod: 2025-04-17T22:57:18+08:00
tags:
 - Python
 - entry
categories: computer
---

Windows 下的 Python 安装第三方库时会在解释器同目录下的子目录 `Scripts` 里
安装很多 100 KB 左右的 exe 文件，执行这些文件可以执行第三方库的某些功能。
最常见的就是 `pip.exe` ，可能存在几个同名文件 `pip3.exe` `pip3.8.exe` 等。

<!--more-->

这不禁让人发问：

- 这个小小的仅有 100 KB 的文件就能包含第三方库的所有功能吗？
- 为什么移动 Python 后 pip 失效了？
- 这些 exe 是怎么生成的？
- 为什么都是 100 KB ，它们之间有什么区别？
- ……

带着这些疑问，我遍寻中文互联网网络，结果果然没让我失望，
几乎千篇一律的抄袭文章，而且全部都是指向一个主题：
教你使用 XXX 将 Python 脚本打包成 exe
。

耐着性子翻捡破烂，不断修改关键词，终于以 `Python Scripts exe` 找到一篇知乎文章
[Python安装目录下Scripts/里的exe文件](https://zhuanlan.zhihu.com/p/360502932) ，这篇文章讲到了 setuptools 的 setup.py 文件，
其中的 setup 函数有一个参数 `entry_points` 是生成 exe 的关键

```python
setup(
    ...,
    entry_points={
        'console_scripts': [
            'xxx = m.s:f', # 示例
        ],
    },
    ...
)
```

搜索关键词 `Python entry_points` 打开了新世界，最终一直找到官方文档以及 pyproject.toml 支持，
详细内容参考链接：

1. <https://zhuanlan.zhihu.com/p/503252479>
2. <https://packaging.python.org/en/latest/specifications/entry-points/#use-for-scripts>
3. <https://python-poetry.org/docs/pyproject/#scripts>
4. <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#a-full-example>

---

**补充**

关于移动 Python 后 pip 失效的问题，如果看完以上资料就明白失效的原因了： pip.exe 内置了 Python 解释器的绝对路径。解决办法就是重新安装 pip 或者更正 pip.exe 内绝对路径，如果是虚拟环境可以选择重建。

**补充二**

pyproject.toml 里定义 `[project.scripts]` 字段即可在安装时生成 entry_points 文件：

```toml
[project.scripts]
foo = demo.cli:main
bar = demo.core.main:main
```

Linux 系统的 entry_points 在 `bin` 目录下，是一个可执行的 python 文件，
其 shebang 指向当前环境的解释器。
对比 Linux 可以发现，Windows 的 entry_points 本质就是将这个 python 文件用
exe 模板包装，查看其字节编码末尾部分，正是该文件的文本内容。
