+++
title = 'rust-analyzer 卡在 fetching metadata'
date = 2023-10-05T13:32:51+08:00
tags = ['rust', 'rust-analyzer']
categories = 'computer'
+++

有时候 rust-analyzer 会卡在 fetching metadata 这一步，
只需要删除 `~/.cargo/.package-cache` 然后重启编辑器就可以了。
