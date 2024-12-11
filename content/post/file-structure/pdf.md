---
title: PDF File Structure
date: 2024-12-11
lastmod: 2024-12-11
draft: true
tags:
 - PDF
 - File Structure
categories: File System
---

最近有一些 PDF 文件需要处理，使用 Adobe Acrobat 编辑十分麻烦，
于是思考编写一个程序来自动化处理 PDF 文件。

先前使用 Python 给 PDF 文件添加目录或者叫书签（bookmark），依稀记得使用过
PyPDF2 、 pikepdf 等库。于是再次捡起 Python ，很快就完成了需求。

Python 程序需要运行时环境和依赖的库，迁移到其他机器上比较麻烦，因此考虑使用
编译型语言重写程序。
首选 Go 语言，查询资料发现 Go 语言有很多处理 PDF 文件的库，如：
gofpdf 、 unipdf 、 pdfcpu 等。
其中 gofpdf 似乎不怎么更新了， unipdf 需要授权才能使用，最终选择了 pdfcpu 。
目前 pdfcpu 发布了 0.9 版本，我感觉 API 不好用。
很简单的一个功能却很难写出来，于是放弃。
之后选择 Rust 语言，有一个 pdf 库，但是 README 声称“写”和“改”处于实验阶段，
然后放弃。
其他语言不在考虑范围。

最终从 Python 官网下载一个嵌入式包，拼合一个可移植的 PDF 处理程序。

---

上面的故事是个引子，是我想要深入理解 PDF 文件结构的原因。
过程不讲。

---

研究 PDF 文件结构，最权威的资料是 ISO 32000-1 ，但是该资料似乎需要付费购买，
又没有渠道，遂放弃。

以下研究主要参考 <https://www.cnblogs.com/Primzahl/p/14735567.html>
以及使用 VSCode 以文本方式打开一个 PDF 文件，观察其内容与结构。

> 单纯阅读标准很抽象很枯燥，最好找一个 PDF 文件，以纯文本的方式打开，对照标准观察结构。

PDF 是一种以标记语言为结构、以流式存储的文件格式。
PDF 主要由四部分组成：

- Header：文件头，包括文件标识、版本、文档信息等。
- Body：文档内容，包括文本、图形、图表、音频、视频等。
- Cross-Reference Table：交叉引用表，记录文档中各个对象在文件中的位置。
- Trailer：文件尾，包括文件偏移量、加密信息等。

在 VSCode 中可以观察到， PDF 文件是有很多行组成。
Header 是 PDF 文件的第一行，通常是 `%PDF-1.X` ，标示文件版本，
其中 X 是 `1-7` 中的一个数字。
随后是一串以 `\d+ \d+ obj` 和 `endobj` 包裹的块，这些块串就是 Body 。
接着以 `xref` 开头的一行，后面跟着交叉引用表。
最后是 `trailer` 开头的一行，后面跟着文件尾， PDF 文件最后一行通常是 `%%EOF`。

一个简单的 PDF 文件结构示例如下：

```
%PDF-1.4
1 0 obj
<</Type/Catalog/Pages 2 0 R>>
endobj
2 0 obj
<</Type/Pages/Kids[3 0 R]/Count 1>>
endobj
3 0 obj
<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R>>
endobj
4 0 obj
<</Length 102>>
stream
BT
/F1 18 Tf
100 600 Td
(Hello World) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f
0000000018 00000 n
0000000077 00000 n
0000000142 00000 n
0000000217 00000 n
trailer
<</Size 5/Root 1 0 R>>
startxref
255
%%EOF
```
