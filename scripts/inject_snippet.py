from pathlib import Path

md_path = Path("zenn-content/articles/greeting-article.md")
snippet_path = Path("zenn-content/snippets/greet.py")

with md_path.open() as f:
    content = f.read()

with snippet_path.open() as f:
    code = f.read()

# 置換
pattern = r'```python\n.*?\n```'
replacement = f'```python\n{code}\n```'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with md_path.open("w") as f:
    f.write(new_content)
