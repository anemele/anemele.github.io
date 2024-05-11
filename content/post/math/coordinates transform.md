---
title: 直角、柱、球坐标系转换
date: 2023-12-26
tags:
 - formula
categories: math
math: true
---

***不知为何无法渲染公式，暂时不用管它。***

---

常用的坐标系有三类：

- 直角坐标系（Cartesian）
- 柱坐标系（Cylindrical）
- 球坐标系（Spherical）

三者都属于*欧氏几何右手*坐标系。

<!--more-->


**定义**

用坐标系原点指向坐标系中任意一点的矢量作为该点的**位置矢量**，简称**位矢**。

位矢在三类坐标系中表示为

$$
\left\{
\begin{aligned}
\vec{A}=A_x{\hat{a}}_x+A_y{\hat{a}}_y+A_z{\hat{a}}_z\\
\vec{A}=A_r{\hat{a}}_r+A_\phi{\hat{a}}_\phi+A_z{\hat{a}}_z\\
\vec{A}=A_r{\hat{a}}_r+A_\theta{\hat{a}}_\theta+A_\phi{\hat{a}}_\phi
\end{aligned}
\right.
$$

## 直角坐标系-柱坐标系

柱坐标和直角坐标之间的转换，其实就是极坐标和平面直角坐标之间的转换，满足下列关系

$$
\left\{\begin{aligned}x=r\cos\phi\\ y=r\sin\phi\end{aligned}\right.
$$

直角坐标系 --> 柱坐标系

变换矩阵

$$
\left[\begin{matrix}{\hat{a}}_r\\{\hat{a}}_\phi\\{\hat{a}}_z\\\end{matrix}\right]=\left[\begin{matrix}\cos{\phi}&\sin{\phi}&0\\-\sin{\phi}&\cos{\phi}&0\\0&0&1\\\end{matrix}\right]\left[\begin{matrix}{\hat{a}}_x\\{\hat{a}}_y\\{\hat{a}}_z\\\end{matrix}\right]
$$

逆变换矩阵（变换矩阵的转置）

$$
\left[\begin{matrix}{\hat{a}}_x\\{\hat{a}}_y\\{\hat{a}}_z\\\end{matrix}\right]=\left[\begin{matrix}\cos{\phi}&-\sin{\phi}&0\\\sin{\phi}&\cos{\phi}&0\\0&0&1\\\end{matrix}\right]\left[\begin{matrix}{\hat{a}}_r\\{\hat{a}}_\phi\\{\hat{a}}_z\\\end{matrix}\right]
$$

## 柱坐标系-球坐标系

柱坐标系 --> 球坐标系

$$
\left[\begin{matrix}{\hat{a}}_r\\{\hat{a}}_{\theta}\\{\hat{a}}_{\phi}\\\end{matrix}\right]=\left[\begin{matrix}\sin{\theta}&0&\cos{\theta}\\\cos{\theta}&0& -\sin{\theta}\\ 0&1&0\\\end{matrix}\right]\left[\begin{matrix}{\hat{a}}_r\\{\hat{a}}_{\phi}\\{\hat{a}}_z\\\end{matrix}\right]
$$

逆变换

$$
\left[\begin{matrix}{\hat a}_r\\{\hat a}_\phi\\{\hat a}_z\\\end{matrix}\right]=\left[\begin{matrix}\sin\theta&\cos\theta&0\\0&0&1\\\cos\theta&-\sin\theta&0\\\end{matrix}\right]\left[\begin{matrix}{\hat a}_r\\{\hat a}_\theta\\{\hat a}_\phi\\\end{matrix}\right]
$$

## 球坐标系-直角坐标系

直角坐标系 --> 球坐标系

$$
\begin{aligned}\left[\begin{matrix}{\hat a}_x\\{\hat a}_y\\{\hat a}_z\end{matrix}\right]&=\left[\begin{matrix}\cos\phi&-\sin\phi&0\\\sin\phi&\cos\phi&0\\0&0&1\end{matrix}\right]\left[\begin{matrix}\sin\theta&\cos\theta&0\\0&0&1\\\cos\theta&-\sin\theta&0\\\end{matrix}\right]\left[\begin{matrix}{\hat a}_r\\{\hat a}_\theta\\{\hat a}_\phi\\\end{matrix}\right]\\&=\left[\begin{matrix}\sin\theta\cos\phi&\cos\theta\cos\phi&-\sin\phi\\\sin\theta\sin\phi&\cos\theta\sin\phi&\cos\phi\\\cos\theta&-\sin\theta&0\end{matrix}\right]\left[\begin{matrix}{\hat a}_r\\{\hat a}_\theta\\{\hat a}_\phi\end{matrix}\right]\end{aligned}
$$

逆变换

$$
\left[\begin{matrix}{\hat a}_r\\{\hat a}_\theta\\{\hat a}_\phi\end{matrix}\right]=\left[\begin{matrix}\sin\theta\cos\phi&\sin\theta\sin\phi&\cos\theta\\\cos\theta\cos\phi&\cos\theta\sin\phi&-\sin\theta\\-\sin\phi&\cos\phi&0\end{matrix}\right]\left[\begin{matrix}{\hat a}_x\\{\hat a}_y\\{\hat a}_z\end{matrix}\right]
$$

