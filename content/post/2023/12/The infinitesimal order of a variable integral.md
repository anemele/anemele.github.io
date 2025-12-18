---
title: 变限积分的无穷小阶
date: 2023-12-26
tags:
 - formula
categories: math
math: true
---

对于

$$
\int_{\phi(x)}^{\varphi(x)}f(x){\rm d}x
$$

其中
$\varphi(x)$、$\phi(x)$、$f(x)$
的无穷小阶数分别是
$n_1$、$n_2$、$m$
，则该变限积分的无穷小阶数等于

$$
\min\\{n_1,n_2\\}\times m+阶数\\{\varphi(x)-\phi(x)\\}
$$

例题：

$$
\int_{x}^{\sin x}(e^{t^2}-1){\rm d}t
$$

阶数为 $1\times2+3=5$
