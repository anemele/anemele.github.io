+++
title = 'Tex 笔记'
date = 2023-06-16T13:32:47+08:00
tags = ['tex']
categories = 'tex'
+++


常用插图语法

```latex
\begin{figure} [htb!]
\centering
\includegraphics[width=20]{相对路径}
\caption{标题}
\label{fig:my-fig}
\end{figure}
```

常用表格语法

```latex
\begin{table}
\centering
\caption{}
\label{tab:my-tab}
\begin{tabular}[|c|]
\hline
1&2
\\\hline
3&4
\\hline
\end{tabular}
\end{table}
```

控制页面-每行字数

[latex如何设置每行字数? - 知乎 (zhihu.com)](https://www.zhihu.com/question/339986171)

```latex
\usepackage{calc}
\usepackage{geometry}
\geometry{a4paper,textwidth=\widthof{一}*\real{35}}
```

标题控制

[LaTeX标题控制 - 简书 (jianshu.com)](https://www.jianshu.com/p/0a1c45a02120)

目录深度控制

[latex让三级标题不在目录显示? - 知乎 (zhihu.com)](https://www.zhihu.com/question/430664521/answer/1584159930)

```latex
\setcounter{tocdepth}{2}
```

