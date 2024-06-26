---
title: base64 编码原理
date: 2023-11-23
tags:
 - encoding
 - base64
categories: computer
---

先前一直有听说 base64 编码应用很广泛，日常也曾调包使用，
但是从未深究其原理，只大概了解它是用 6 bit 表示 8 bit 的信息。

前几天玩 ctf 遇到了一个用六十四卦包装的 base64 编码，
不得不深入学习 base64 。


<!--more-->

凭着印象，用 Python 实验，探索出 base64 的原理，其实很简单。

一个字节是 8 bit，其中包含很多无法显示的字符、空白字符、或者其它字符。
base64 做的事情就是使用 64 个基本字符对原比特流重新编码。

这 64 个字符是：大写字母、小写字母、阿拉伯数字、加号、斜杠
，即 `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`
，按顺序对应二进制 `000000` 到 `111111`
。实际使用时有 65 个字符，多的一个 `=` 后面再说。

下面具体实验：

随便选一个字符，如字符 `'0'` 的 ASCII 编码是 `00110000`
。由于 base64 是 6 比特每字符，为了方便，先取 3 个字符对齐，即 `'000'`
，其 ASCII 编码为 `001100000011000000110000`
，每 6 位分割，得到 `001100,000011,000000,110000`
，查表可以得到 base64 编码为 `MDAw` 。

```python
import base64

print(base64.b64encode('000'))
# MDAw
```

验证无误。

思考：
字节流的比特数是 8 的倍数， base64 流的比特数要求是 6 的倍数，
那么 8n % 6 一定会有余数（ 2 或 4 ）。
多余的比特无法用 base64 编码，怎么办呢？

先实验看结果做猜想：

```python
print(base64.b64encode('00'))
# MDA=

print(base64.b64encode('0'))
# MA==
```

有多余比特的 base64 编码结尾出现了 `=` 字符。

`'00'` 多余 4 个比特，结尾 1 个 `=`；`'0'` 多余 2 个比特，结尾 2 个 `=`。
可以猜测 `=` 的作用是填充比特，1 个 `=` 等于 2 个比特。

再看 `'00'` 多余的比特是 `0000`，`'0'` 多余的比特是 `00` ，
结尾均出现了 `A` （ `000000` ），
可以猜测填充的比特是 `00` ，即 1 个 `=` 等于 `00` 。

为验证猜想，另选几个字符做实验

```python
print(base64.b64encode('1'))
# 001100,01 --> MQ==

print(base64.b64encode('11'))
# 001100,010011,0001 --> MTE=
```

符合猜想。

结论：

计算机中的数据本质上都是比特流，根据不同的规则解释出不同的语义。
例如，根据约定，将连续的 8 个比特按照一定的映射规则（ ASCII 表）
组成字节序列，其中可见字符序列就是文本。
base64 就是另一种映射规则罢了。