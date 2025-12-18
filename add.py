#!/usr/bin/python
"""Add new post."""

from datetime import datetime
from pathlib import Path

post_name = input("post name(.md):  ").strip()
if post_name == "":
    print("empty and exit.")
    exit()
if not post_name.endswith(".md"):
    post_name = f"{post_name}.md"

this_path = Path(__file__).parent
year_month = datetime.today().strftime("%Y/%m")
target_path = this_path / "content/post" / year_month
# print(target_path)
target_path.mkdir(parents=True, exist_ok=True)

post_path = target_path / post_name
try:
    post_path.touch()
    post_path = post_path.relative_to(this_path)
    print(f"edit file:  {post_path}")
except OSError as e:
    print(e)
