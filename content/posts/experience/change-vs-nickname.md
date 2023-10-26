+++
title = 'Visual Studio 修改别名'
date = 2023-05-03T15:13:56+08:00
tags = ['Visual Studio', 'rename']
categories = 'computer'
+++

Edit files in two places:

1. `%ProgramFiles%\Microsoft Visual Studio\[year]\[Version]\Common7\IDE\*.isolation.ini`
2. `%ProgramData%\Microsoft\VisualStudio\Packages\_Instances\{InstanceId}\state.json`

Change or modify the `Nickname` value. Require run as Admin.

# Reference

1. <https://developercommunity.visualstudio.com/t/not-able-to-easiliy-change-installation-nickname/99059#T-N384658>
