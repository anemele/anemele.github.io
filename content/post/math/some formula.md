+++
title = '一些公式'
date = 2023-12-26T17:41:37+08:00
tags = ['']
categories = 'math'
math = true
+++

记录一些公式，排列较为混乱，凑合看看吧。

# 三次方差公式

$$
(a+b)^3=a^3+b^3+3ab^2+3a^2b\\\\
\Downarrow\\\\
a^3+b^3\\\\
=(a+b)^3-3ab(a+b)\\\\
=(a+b)(a^2+b^2+2ab-3ab)\\\\
=(a+b)(a^2+b^2-ab)\\\\
\Downarrow\\\\
a^3+b^3=(a+b)(a^2+b^2-ab)
$$

同理可得

$$
a^3-b^3=(a-b)(a^2+b^2+ab)
$$

应用：

$$
x^6+1=(x^2+1)(x^4+1-x^2)
$$

# 幂函数泰勒级数

$$
(1+x)^\alpha=\sum\limits_{n=0}^{\infty}\dfrac{A_\alpha^n}{n!}x^n
$$

# 幂函数×指数函数不定积分

（a 小于 0 的情况使用伽马函数，a 大于 0 先换元）

$$
\int t^ne^{at}{\rm d}x=e^{at}\sum\limits_{k=0}^n(-1)^k\dfrac{A_n^k}{a^{k+1}}t^{n-k}
$$

$$
\int te^{t}{\rm d}t=e^{t}(t-1)
$$

$$
\int t^2e^t{\rm d}t=e^t(2-2t+t^2)
$$

# 欧拉方程

$$
\sum\limits_{k=0}^{n}a_kx^ky^{(k)}=f(x)
$$

$$
x^ky^{(k)}=A_D^ky=\prod\limits_{i=0}^{k}(D-i)y=D(D-1)\dots(D-k+1)y
$$

# 抽样分布定理

$$
\dfrac{\bar X-\mu}{\sigma/\sqrt{n}}\sim N(0,1)
$$

$$
\dfrac{\bar X-\mu}{S/\sqrt{n}}\sim t(n-1)
$$

$$
(n-1)\dfrac{S^2}{\sigma^2}\sim \chi^2(n-1)
$$

$$
\dfrac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{\dfrac{\sigma_1^2}{n}+\dfrac{\sigma_2^2}{m}}}\sim N(0,1)
$$

$$
\dfrac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_\omega\sqrt{\dfrac{1}{n}+\dfrac{1}{m}}}\sim t(n+m-2)
$$

$$
S_\omega^2=\dfrac{(n-1)S_1^2+(m-1)S_2^2}{n+m-2}
$$

$$
\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F(n-1,m-1)
$$

$$
\chi^2(n)=\sum\limits_{k=1}^{n}X_k^2
$$

$$
t(n)=\dfrac{X}{\sqrt{Y/n}}
$$

$$
F(n,m)=\dfrac{\chi^2(n)/n}{\chi^2(m)/m}
$$

# 切比雪夫不等式

$$
P\{|X-EX|\geqslant\varepsilon\}\leqslant\dfrac{DX}{\varepsilon^2}
$$

# 一阶线性微分方程通解公式

$$
y'+P(x)y=Q(x)
$$

$$
y(x)=e^{-\int P(x){\rm d}x}[\int Q(x)e^{\int P(x){\rm d}x}{\rm d}x+C]
$$

# 华莱士公式

$$
\int_{0}^{\frac{\pi}{2}}\sin^nx{\rm d}x=
\int_{0}^{\frac{\pi}{2}}\cos^nx{\rm d}x=
\dfrac{(n-1)!!}{n!!}\cdot(1\\;if\\;n\\&1\\;else\\;\dfrac{\pi}{2})
$$

# 高斯公式

$$
\oiint P{\rm d}y{\rm d}z+Q{\rm d}x{\rm d}z+R{\rm d}x{\rm d}y=\iiint (\dfrac{\partial P}{\partial x}+\dfrac{\partial Q}{\partial y}+\dfrac{\partial R}{\partial z}){\rm d}v
$$

散度

$$
\nabla F=\dfrac{\partial^2 F}{\partial x^2}+\dfrac{\partial^2 F}{\partial y^2}+\dfrac{\partial^2 F}{\partial z^2}
$$

# 斯托克斯公式

$$
\oint P{\rm d}x+Q{\rm d}y+R{\rm d}z=\iint\bf{rot\;F}{\rm d}S
$$

旋度

$$
\nabla\times F=\left|\begin{matrix}{\bf i}&{\bf j}&{\bf k}\\\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\\\F_x&F_y&F_z\end{matrix}\right|
$$

# 斯托克斯公式①

$$
\oint P{\rm d}x+Q{\rm d}y+R{\rm d}z=\iint\left|\begin{matrix}{\rm d}y{\rm d}z&{\rm d}x{\rm d}z&{\rm d}x{\rm d}y\\\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\\\F_x&F_y&F_z\end{matrix}\right|
$$

# 斯托克斯公式②

$$
\oint P{\rm d}x+Q{\rm d}y+R{\rm d}z
=\iint
\left|\begin{matrix}\cos\alpha&\cos\beta&\cos\gamma\\\\
\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\\\
F_x&F_y&F_z
\end{matrix}\right|
{\rm d}S
$$

# 幂指函数泰勒公式

$$
x^x=e^{x\ln x}=\sum\limits_{n=0}^{\infty}\dfrac{(x\ln x)^n}{n!}
$$

# 一个无穷小

$$
1-\cos^\alpha x=-[(1-\sin^2x)^{\frac{a}{2}}-1]\sim-[-\dfrac{\alpha}{2}\sin^2(x)]\sim\dfrac{\alpha}{2}x^2
$$

# 搞笑公式

$$
\lim\limits_{n\to0}\dfrac{sinx}{n}=six=6
$$

# 伽马函数

$$
\Gamma(x)=\int_{0}^{+\infty}t^{x-1}e^{-t}{\rm d}t,\;x>0
$$

$$
\Gamma(\dfrac12)=\sqrt\pi,\;\Gamma(1)=1
$$

$$
\Gamma(x+1)=x\Gamma(x),\;\Gamma(n+1)=n!
$$

# 斯特林公式

$$
\lim\limits_{n\to\infty}n!=\sqrt{2\pi n}(\dfrac ne)^n
$$

# $\tan^nx$ 积分

$$
\int\tan^nx{\rm d}x=\dfrac{\tan^{n-1}x}{n-1}-\int\tan^{n-2}x{\rm d}x
$$

# $\ln(x+\sqrt{x^2+1})$ 泰勒展开式

首先求导，得到 $\dfrac{1}{\sqrt{x^2+1}}$，泰勒展开为 $1-\dfrac12x^2+o(x^2)$，再积分，得到 $x-\dfrac16x^3+o(x^3)$，即

$$
\ln(x+\sqrt{x^2+1})=x-\dfrac16x^3+o(x^3)
$$

# 自然数和公式

自然数和是初项和公差都为 1 的等差数列

$$
1+2+\dots+n=\dfrac{n(n+1)}{2}
$$

# 平方和公式

$$
\sum\limits_{i=1}^{n}i^2=\dfrac{n(n+1)(2n+1)}{6}
$$

# 立方和公式

$$
\sum\limits_{i=1}^{n}i^3=(\sum\limits_{i=1}^{n}i)^2=(\dfrac{n(n+1)}{2})^2=\dfrac{n^2(n+1)^2}{4}
$$

```julia
f1(n)=sum((1:n).^3)
f2(n)=n^2*(n+1)^2/4
a=1:100
@assert all(f1.(a)==f2.(a))
```
