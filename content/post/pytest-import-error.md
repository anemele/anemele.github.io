---
title: pytest 遇到 import 导入错误
date: 2024-01-19
tags:
 - pytest
 - import
categories: computer
---

pytest 是很好用的 Python 测试框架，比标准库 unittest 好用太多。

Python 的一个包就是一个文件夹，通常包含 `__init__.py` 文件。

例如

```text
foo/
  |- __init__.py
```

可以使用 `import foo` 或者 `from foo import xxx` 导入 `foo` 包。

Python3K 无需该文件也可，问题就出现在这里。

通常的 `__init__.py` 文件都是空文件，为了方便选择不创建。
但是 pytest 会报错（具体内容忘了，大概是导入错误），此时只需创建 `__init__.py` 文件即可解决。
