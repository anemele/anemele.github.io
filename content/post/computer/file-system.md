+++
title = '操作系统——文件系统'
date = 2023-10-29T14:43:47+08:00
draft = true
tags = ['os', 'file','system']
categories = 'computer'
+++


<!--more-->

文件是一个抽象数据结构，主要由 `元信息` 和 `数据` 组成。
操作系统通过文件控制块（File Control Block, FCB）管理文件， FCB 记录了文件的元信息。
如果没有 FCB ，“数据”将成为散乱无章的噪音，是没有任何意义的。

> 计算机内部的数据在形式上都是一串 01 ，经过特定的规则解释，才形成各种文件。
