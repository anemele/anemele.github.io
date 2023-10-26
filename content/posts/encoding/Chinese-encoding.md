+++
title = '中文乱码分析'
date = 2023-09-24T11:53:49+08:00
tags = ['encoding']
categories = 'computer'
+++

由于世界各地文字多样，计算机世界产生了很多编码。
编码就是以一种规则解释二进制机器码，不同文字的机器码是一样的，都是 `0101` 序列。
因此以一种方式编码，再以另一种方式解码就可能产生乱码。

<!--more-->

>不知道乱码的英文是什么？

# 中文乱码

以中文编码为例，中文编码主要包括

- GBK
- GB2312（大陆制定的简体字编码）
- BIG5（台湾制定的繁体汉字编码）
- UTF-8
- ISO8859-1

> ISO8859-1 无法编码汉字？

# 常见乱码

（Python 程序生成，错误处理方式默认 strict，出现错误采用 replace）

| 码名 | 示例 | 特征 | 原因 |
| :----: | :----: | :----: | :----: |
| 原码 | 你好，很高兴认识你。现在我来向你展示计算机编解码错误导致的乱码。 |  |  |
| 方块码 | ��ã��ܸ�����ʶ�㡣������������չʾ��������������µ����롣 | 黑底问号方块 | GBK 编码，UTF-8 解码 |
| 古文码 | 浣犲ソ锛屽緢楂樺叴璁よ瘑浣犮�傜幇鍦ㄦ垜鏉ュ悜浣犲睍绀鸿�＄畻鏈虹紪瑙ｇ爜閿欒��瀵艰嚧鐨勪贡鐮併�� | 古文夹杂日韩文 | UTF-8 编码，GBK 解码 |
| 拼音码 | ÄãºÃ£¬ºÜ¸ßÐËÈÏÊ¶Äã¡£ÏÖÔÚÎÒÀ´ÏòÄãÕ¹Ê¾¼ÆËã»ú±à½âÂë´íÎóµ¼ÖÂµÄÂÒÂë¡£ | 带帽的字母 | GBK 编码，ISO8859-1 解码 |
| 符号码 | ä½ å¥½ï¼å¾é«å´è®¤è¯ä½ ãç°å¨ææ¥åä½ å±ç¤ºè®¡ç®æºç¼è§£ç éè¯¯å¯¼è´çä¹±ç ã | 奇怪的符号 | UTF-8 编码，ISO8859-1 解码 |
| 问号码 | 你好，很高兴认识你�?�现在我来向你展示�?�算机编解码错�??导致的乱码�?? | 大部分正常，结尾有问号 | UTF-8 编码，GBK 解码后再编码，UTF-8 解码 |
| 锟斤拷码 | 锟斤拷茫锟斤拷芨锟斤拷锟斤拷锟绞讹拷恪ｏ拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟秸故撅拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟铰碉拷锟斤拷锟诫。 | 锟斤拷 | GBK 编码，UTF-8 解码后再编码，GBK 解码 |

---

# 附 Python 程序

```python
table = [
    ('码名', '示例', '特征', '原因'),
    (':----:', ':----:', ':----:', ':----:'),
]

# 原码
word = '你好，很高兴认识你。现在我来向你展示计算机编解码错误导致的乱码。'
table.append(('原码', word, '', ''))

# 编解码错误的处理方式包括：strict(by default), ignore, replace, e.t.c.
# 以下默认采用 strict，有错误采用 replace

# GBK 编码，UTF-8 解码
table.append(
    (
        '方块码',
        word.encode('gbk').decode('utf-8', errors='replace'),
        '黑底问号方块',
        'GBK 编码，UTF-8 解码',
    )
)

# UTF-8 编码，GBK 解码
table.append(
    (
        '古文码',
        word.encode('utf-8').decode('gbk', errors='replace'),
        '古文夹杂日韩文',
        'UTF-8 编码，GBK 解码',
    )
)

# GBK 编码，ISO8859-1 解码
table.append(
    (
        '拼音码',
        word.encode('gbk').decode('iso8859-1', errors='replace'),
        '带有注音符号的字母',
        'GBK 编码，ISO8859-1 解码',
    )
)

# UTF-8 编码，ISO8859-1 解码
table.append(
    (
        '符号码',
        word.encode('utf-8').decode('iso8859-1', errors='replace'),
        '奇怪的符号',
        'UTF-8 编码，ISO8859-1 解码',
    )
)

# ISO8859-1 无法编码汉字？
# word.encode('iso8859-1','ignore') == b''

# UTF-8 编码，GBK 解码后再编码，UTF-8 解码
table.append(
    (
        '问号码',
        word.encode('utf-8')
        .decode('gbk', errors='replace')
        .encode('gbk', errors='replace')
        .decode('utf-8', errors='replace'),
        '大部分正常，结尾有问号',
        'UTF-8 编码，GBK 解码后再编码，UTF-8 解码',
    )
)

# GBK 编码，UTF-8 解码后再编码，GBK 解码
table.append(
    (
        '锟斤拷码',
        word.encode('gbk')
        .decode('utf-8', errors='replace')
        .encode('utf-8', errors='replace')
        .decode('gbk', errors='replace'),
        '锟斤拷',
        'GBK 编码，UTF-8 解码后再编码，GBK 解码',
    )
)


# --- 生成 Markdown 表格 --- #
with open('./table.md', 'w', encoding='utf-8') as fp:
    for line in table:
        fp.write('| {} |\n'.format(' | '.join(line)))

```
