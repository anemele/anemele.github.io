---
title: Windows 动态链接库找寻顺序
date: 2023-12-26
tags:
 - dll
 - Windows
categories: computer
---

动态链接库是一种共享程序文件，Windows 下后缀名为 .dll (dynamic link library) ，Linux 下为 .so (shared object) 。

> Windows 下可执行文件 exe 寻找 dll 的顺序依次为：
>
> 1.  exe 所在路径
> 2.  C:\Windows\System32
> 3.  C:\Windows
> 4.  当前路径
> 5.  环境变量中其他路径

*实际上，系统路径（System32）与Windows 路径也在环境变量，属于系统环境变量，优先级较高。*
