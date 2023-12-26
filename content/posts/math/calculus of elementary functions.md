+++
title = '常用初等函数微积分'
date = 2023-12-26T16:48:56+08:00
tags = ['']
categories = 'math'
enableLaTeX = true
+++

12 个微分/导数，13 个积分。

*不定积分需要 $+C$，下面都省略了。验证两个不定积分结果是否相等的方法是求导。*

|导数|积分|
|--|--|
|$(x^n)'=nx^{n-1}$|$\int x^n{\rm d}x=\dfrac{x^{n+1}}{n+1}$|
|$(e^x)'=e^x$|$\int e^x{\rm d}x=e^x$|
|$(a^x)'=a^x\ln a$|$\int a^x{\rm d}x=\dfrac{a^x}{\ln a}$|
|$(\ln x)'=\dfrac1x$|$\int\ln x{\rm d}x=x\ln x-x$|
|$(\log_ax)'=\dfrac1{x\ln a}$|$\int\log_ax{\rm d}x=\dfrac{1}{\ln a}(x\ln x-x)$|
|$\sin'x=\cos x$|$\int\sin x{\rm d}x=-\cos x$|
|$\cos'x=-\sin x$|$\int\cos x{\rm d}x=\sin x$|
|$\tan'x=\sec^2x$|$\int\tan x{\rm d}x=$|
|$\cot'x=\sec^2x$|$\int\cot x{\rm d}x=$|
|$\sec'x=\sec^2x$|$\int\sec x{\rm d}x=$|
|$\csc'x=\sec^2x$|$\int\csc x{\rm d}x=$|
||$\int\dfrac{1}{x^2-a^2}{\rm d}x=\dfrac{1}{2a}\ln\dfrac{x-a}{x+a}$|
||$\int\dfrac{1}{x^2+a^2}{\rm d}x=$|
||$\int\dfrac{1}{x^2+a^2}{\rm d}x=$|
|||
|$[\ln(x+\sqrt{x^2+1})]'=\dfrac{1}{\sqrt{1+x^2}}$|