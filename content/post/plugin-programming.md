---
title: 插件式编程
date: 2023-12-26
tags:
 - plugin
 - programming
categories: computer
---

遇到某些情况，循环内的条件在循环开始前就确定了，但只是给原来增添一些功能，为了代码复用，不必写在外边。

这就造成了冗余判断。

```python
def func(cond: bool):
    for i in range(100):
        do1
        if cond:
            do2
```

避免冗余 if 的方法

```python
def func(cond: bool):
    if cond:
        for i in range(100):
            do1
            do2
    else:
        for i in range(100):
            do1
```

但是这样写起来很麻烦，只是增添一点点功能，就要重复大量代码。

另一种相似的情况，条件选择执行模块

```python
def func(cond: bool):
    for i in range(100):
        if cond:
            do1
        else:
            do2
```

写成

```python
def func(cond: bool):
    if cond:
        for i in range(100):
            do1
    else:
        for i in range(100):
            do2
```

这个可以用函数，但又增添了栈成本

```python
def func(cond: bool):
    do = do1 if cond else do2
    for i in range(100):
        do
```

一个理想的方式，姑且称为插件式编程，但不得思路，也不知道可行与否。
