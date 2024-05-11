---
title: 二阶常系数线性齐次微分方程共轭复根通解思考
date: 2023-11-21
tags:
 - differential equation
categories: math
math: true
---

二阶常系数线性齐次微分方程形如：

$$
y''+Py'+Qy=0
$$

根据特征方程 $r^2+Pr+Q=0$ 的解得到通解，分为 3 种情况：

- 两异实根 $r_1,r_2$ ， $y=C_1e^{r_1x}+C_2e^{r_2x}$
- 两同实根 $r$ ， $y=(C_1+C_2x)e^{rx}$
- 共轭复根 $\alpha\pm i\beta$ ， $y=e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$

下面是一个思考：

两同实根的情况暂无考虑。
共轭复根与两异实根都是两个不同的根，实根可以看作虚部为 $0$ 的复根。那么共轭复根情况的通解是否可以写作
$y=C_1e^{(\alpha+i\beta)x}+C_2e^{(\alpha-i\beta)x}$
呢？

化简得到
$y=e^{\alpha x}(C_1e^{i\beta x}+C_2e^{-i\beta x})$
，与通解的形式很相似了。
如果二者相等，即
$C_1e^{i\beta x}+C_2e^{-i\beta x}=C_1\cos\beta x+C_2\sin\beta x$
。这一步是如何得到呢？
如果得不到就说明一开始就是错误的，共轭复根的通解不能像两异实根那样写。

（待定）