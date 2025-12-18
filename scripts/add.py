#!/usr/bin/python
"""Add new post."""

from datetime import date
from pathlib import Path


post_name = input("post name: ").strip()
if post_name == "":
    print("empty and exit.")
    exit()

this_path = Path(__file__).parent.parent
today = date.today()
target_path = this_path / "content/post" / today.strftime("%Y/%m")
# print(target_path)

if post_name.endswith("/"):
    post_path = target_path / post_name
    if post_path.parent != target_path:
        print("invalid post name!")
        exit()
    post_name = "index.md"
else:
    post_path = target_path
    if not post_name.endswith(".md"):
        post_name = f"{post_name}.md"

post_path.mkdir(parents=True, exist_ok=True)
post_path = post_path / post_name

title_tmpl = f"""\
---
title: name
date: {today}
lastmod: {today}
draft: true
tags:
 - tag
categories:
 - category
---\n\n
"""

try:
    post_path.write_text(title_tmpl)
    post_path = post_path.relative_to(this_path)
    print(f"edit file: {post_path}")
except OSError as e:
    print(e)
