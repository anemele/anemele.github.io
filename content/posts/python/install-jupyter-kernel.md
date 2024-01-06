+++
title = '安装 Jupyter kernel'
date = 2024-01-06T14:19:58+08:00
tags = ['jupyter', 'kernel']
categories = 'Jupyter'
featured_image = '/images/Jupyter.svg'
+++

Jupyter 是一个对于交互式编程十分友好的工具。

Jupyter 是使用 Python 开发的 Web 程序，

<!--more-->

最初为了支持 Python 在科学计算方面的应用，
之后开发人员为 Jupyter 添加了很多内核，使其可以支持更多编程语言，具体参考
<https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>
。

# 安装 Jupyter

早期的 Jupyter 环境是 notebook ，现在推荐使用 lab 。
首先要有 Python 环境（可以创建一个虚拟环境），使用 pip 安装

```bash
pip install jupyterlab
```

等待安装完成。
jupyterlab 自带一个默认的 Python 内核，名为 `ipykernel` 。

# 内核操作

## 列出内核

```bash
jupyter-kernelspec list
```

## 删除内核

```bash
jupyter-kernelspec remove {name}
```

## 安装内核

### Python

（创建一个虚拟环境）

```bash
python -m pip install ipykernel
python -m ipykernel --version
python -m ipykernel install --user --name {} --display-name {}
```

### Julia

```julia
using Pkg
Pkg.add("IJulia")
using IJulia
installkernel("Julia")
```

### R

```r
install.packages('devtools', type='binary')
devtools::install_github('IRkernel/IRkernel')
```
or
```r
install.packages('IRkernel')
IRkernel::installspec()
```

### JavaScript

```JavaScript
npm i -g ijavascript
```

### Java

下载内核
[SpencerPark/IJava](https://github.com/SpencerPark/IJava)
然后执行 `install.py`
