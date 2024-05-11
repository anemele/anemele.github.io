+++
title = '常用随机分布'
date = 2024-01-10T21:03:37+08:00
tags = ['']
categories = 'math'
math = true
+++

|名称|参数|概率公式|期望|方差|
|--|--|--|--|--|
|二项分布|$n\ge1;p;k\ge0;$|$C_n^kp^kq^{n-k}$|$np$|$npq$|
|几何分布|$p;k\ge1;$|$pq^{k-1}$|$\dfrac{1}{p}$|$\dfrac{q}{p^2}$|
|超几何分布|$N,M,n,k$|$\dfrac{C_M^kC_{N-M}^{n-k}}{C_N^n}$|||
|泊松分布|$\lambda\gt0;k\ge0;$|$\dfrac{\lambda^k}{k!}e^{-\lambda}$|$\lambda$|$\lambda$|
|均匀分布|$a\lt b$|$\dfrac{1}{b-a}[u(x-a)-u(x-b)]$|$\dfrac{a+b}{2}$|$\dfrac{(a-b)^2}{12}$|
|指数分布|$\lambda\gt0$|$\lambda e^{-\lambda x}\\;if\\;x\gt0\\;else\\;0$|$\dfrac{1}{\lambda}$|$\dfrac{1}{\lambda^2}$|
|正态分布|$\mu;\sigma\gt0$|$\dfrac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(\mu-x)^2}{2\sigma^2}}$|$\mu$|$\sigma^2$|
