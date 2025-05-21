from pathlib import Path

md_path = Path("zenn-content/articles/greeting-article.md")
snippet_path = Path("zenn-content/snippets/greet.py")

with md_path.open() as f:
    content = f.read()

with snippet_path.open() as f:
    code = f.read()

# 置換
new_content = content.replace(
    "```python\n<!-- snippet:greet.py -->\n```",
    f"```python\n{code}\n```"
)

with md_path.open("w") as f:
    f.write(new_content)
