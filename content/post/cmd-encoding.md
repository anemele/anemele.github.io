---
title: Windows 命令行编码
date: 2022-02-21
tags:
 - encoding
 - Windows
 - cmd
categories: computer
---

<!--more-->

Windows10 家庭中文版的命令行默认编码是 GBK ，运行 UTF-8 编码的程序会出现乱码。

这时需要使用 `chcp` 命令，创建新的编码环境。这个环境是临时的，关闭命令行重启后，仍是 GBK 编码。

直接运行 `chcp` 会返回当前编码的编号，修改编码需要跟上目标编码的编号。

常用编码以及对应编号

| 编码   | 编号  |
| ------ | ----- |
| GBK    | 936   |
| MS-DOS | 437   |
| UTF-8  | 65001 |
