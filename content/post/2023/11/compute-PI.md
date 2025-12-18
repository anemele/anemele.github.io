---
title: 计算圆周率
date: 2023-11-05
tags:
 - PI
 - series
categories: algorithm
math: true
---

圆周率的计算更多的是数学问题，但计算机的算力很大程度上推进了圆周率算法的研究。


<!--more-->



除了古人的巧妙方法，传统算法一般是计算与圆周率有关的级数一定精度的值，然后求解。
例如 $\arctan 1=\dfrac\pi4$，其中级数

$$\arctan x=\sum\limits_{n=0}^{\infty}(-1)^n\dfrac{x^{2n+1}}{2n+1}$$

那么

$$\dfrac{\pi}{4}=\sum\limits_{n=0}^{\infty}(-1)^n\dfrac{1}{2n+1}=1-\dfrac13+\dfrac15\dots$$

取一定精度后计算得到一个确切的值 $x$ ，那么圆周率的计算结果就是 $\pi=4x$。

当然 $\arctan x$ 的收敛速度很慢，计算效率很差，只是举例而已。
现有很多知名级数，包括拉马努金的一系列级数，计算圆周率的收敛速度很快，只需前几项即可达到小数点后几十位上百位的精度。
