+++
title = 'ipynb 导出 PDF'
date = 2023-06-22T22:08:02+08:00
draft = false
tags = ['jupyter', 'PDF']
categories = 'computer'
+++


Jupyter Notebook 是很好的编辑器，甚至可以用来写文章。

写好的 notebook 如何分享给别人呢？

最好的情况是对方拥有 jupyter 环境，直接分享 ipynb 文件。

如果对方不具备相关环境，或者只想阅读无需执行，导出 PDF 是更好的选择。


<!--more-->


# 基本方法

Jupyter Notebook 文件导出 PDF 需要配置一系列外部工具。

首先 Jupyter 安装完整。

安装 nbconvert 包 `pip install nbconvert`

安装 pandoc 和 inkscape，并添加到环境变量。

（还需 latex 环境，可以 miktex，也可 texlive。我早先学用 tex，安装了 texlive，忽略了这一步）

之后，在打开的笔记本界面，选择“文件” - “保存并导出笔记本为”，等待一会，浏览器会下载一个 PDF 文件，即是。

# 支持中文

存在一个问题，导出的 PDF 不支持中文，所有中文显示空白。

一个解决方案是先导出 tex，修改配置再手动编译。

[anaconda jupyter notebook \_.ipynb 文件转 \_.pdf 文件 含中文解决方案\_CHAOS\_ORDER 的博客-CSDN 博客](https://blog.csdn.net/chaos_order/article/details/101114270)

在 tex 文件导言区开篇添加

```latex
\usepackage{fontspec, xunicode, xltxtra}
\setmainfont{Microsoft YaHei}
\usepackage{ctex}
```

然后编译

```bash
xelatex demo.tex
```

另一个解决方案是先导出 markdown，再用 pandoc 导出 PDF。

相比较而言，导出 tex 更能保持 ipynb 原格式。

***

# 一劳永逸

以上方法都是手执鼠标点点而已，还需解压文件，修改配置，手动编译。曾欲写一脚本自动解压、修改、编译，奈何不得编译命令。

又思虑，ipynb 导出 PDF 是用 nbconvert 库，玄机必藏其中。阅读源码，不得其义。

又搜索网络，得知修改 `nbconvert\templates\latex\base.tplx` 文件可行。

*   [修复 Jupyter Notebook 导出 PDF 中文无法显示的问题 (nova.moe)](https://nova.moe/fix-jupyter-export-pdf-cjk-display-problem/)
*   [已解决：一劳永逸解决 jupyter 转 pdf 时中文无法转换问题。\_jupyter 转 pdf 失败\_Tony Einstein 的博客-CSDN 博客](https://blog.csdn.net/qq_42658739/article/details/107544863)

然而不得其文件。

又得一文 [如何找到 nbconvert 中的 tplx 文件并修改？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/427092422/answer/1540059677)，
如其配置。但不知如何写 tplx 文件。

又得一文 [Mac 环境下 jupyter notebook 导出 PDF 显示中文的解决方案 (nbconvert 6, python 3.9)\_mac jupyter 导出 pdf\_lovelegend2121 的博客-CSDN 博客](https://blog.csdn.net/lovelegend2121/article/details/119150858)，
以及文档 [Creating Custom Templates for nbconvert — nbconvert 7.2.9 documentation](https://nbconvert.readthedocs.io/en/latest/customizing.html)，
方知新版本 nbconvert 将模板位置更改为 `\share\jupyter\nbconvert\templates\latex`，修改其中文件，可自定义。

支持中文，可在 base.tex.j2 约 17 行添加 `\usepackage{ctex}`。（j2 约是 jinja2，模板文件）

至此，再导出 pdf 可支持中文。
