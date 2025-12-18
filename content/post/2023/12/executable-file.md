---
title: 可执行文件
date: 2023-12-26
tags:
 - exe
 - PE
categories: computer
---

## 可执行文件格式

Windows 的可执行文件（包括 EXE DLL SYS COM 等）使用 PE（Portable Executable）文件格式。

Linux 使用 ELF（Executable and Linkable Format）文件格式。

Mac 使用 mach-O 文件格式。

Unix-Like 的通用对象文件格式（COFF, Common Object File Format）是很多文件格式的共同祖先，如目标对象文件（.obj  .o）。

*文件格式与后缀名没有直接关系。*

*可执行包括直接执行与间接调用。*

## PE

PE 结构可在编译器头文件库查看。

参考 [初识 PE 头](https://www.cnblogs.com/cunren/p/15575159.html)，
可以编写一个识别可执行程序架构（x86 x64）的程序。
