+++
title = '斐波那契数'
date = 2023-11-05T19:06:01+08:00
tags = ['']
categories = 'algorithm'
math = true
+++


斐波那契数列 Fibonacci 是一个经典数列问题，应用十分广泛。


<!--more-->


其递推定义如下：

$$
f(0)=1 \quad f(1)=1 \quad f(n)=f(n-1)+f(n-2)
$$

按照定义直接编写程序很容易爆栈，稍微大一点的数就无法计算，如 100，更不用说成千上万了。

```python
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)
```

经典的方法是动态规划，可以很轻松计算 100\_000 ：

```python
def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
	return a
```

还有更多高效算法，如矩阵快速幂。
