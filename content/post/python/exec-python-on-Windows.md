+++
title = 'Windows 设置 python 可执行'
date = 2023-12-20T13:25:15+08:00
tags = ['shebang','python','Windows']
categories = 'python'
+++

## 前言

Linux 系统中，给 Python 文件（ .py ）首行注明 `#!/usr/bin/env python` ，再 `chmod +x` 即可给该文件可执行权限。

Windows 系统则不同。

<!--more-->

## 正文

Windows 依据文件后缀名识别文件类型，以及选择打开方式，默认的的可执行文件包括：`com exe bat cmd ...`

Windows 要类似 bat 地注册 py 为可执行脚本，只需右键选择一个 .py 文件，
设置打开方式为指定的 Python 解释器即可。

自 [Python3.3][^1] 起，Windows 安装包附带了一个 python-launcher 工具，安装时选择
`Associate files with Python` 会自动将 .py 文件与 `py.exe` 关联起来，即
.py 文件变成了可执行文件。

此时只需要编写一个 hello.py 文件

```python
print('Hello Python!')
```

打开 cmd 运行 `hello.py`
即可看到屏幕输出 `Hello Python!` 。

如果系统安装了多个版本的 Python ，可以使用 [shebang][^2] 指定。

例如

```python
#!/usr/bin/python3.8
import sys
print(sys.version)
```

会输出 `3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]`
。可以简写为 `python3.8` 。

```python
#!python3.12
import sys
print(sys.version)
```

会输出 `3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]`

更多参考 [python-launcher 用法][^1] 。

---

## 补充

### 虚拟环境

虚拟环境的 Python 解释器可以使用绝对路径，
事实上，Scripts 目录下的 exe 文件都是内置绝对路径的入口文件（entry-point）
，这也是虚拟环境移动后 exe 文件失效的原因。

```python
#!/path/to/venv/python.exe

# 例如
#!C:/Users/admin/python/venv/Scripts/python.exe
```

### PATHEXT

注意到以上执行 .py 文件必须带有 `.py` 后缀名，如 `hello.py`
，如何像 exe bat 等文件一样只输入文件名 `hello` 就可以执行呢？

关键在于两点：

1. 设置 PATHEXT： `环境变量 - 系统变量 - PATHEXT` 添加 `.PY`
2. 将 `.py` 文件所在路径加入 `PATH` ：建立一个目录专门存放 Python 脚本，然后将该目录加入 `PATH`

[^1]: https://docs.python.org/3/using/windows.html#python-launcher-for-windows
[^2]: https://docs.python.org/3/using/windows.html#shebang-lines
