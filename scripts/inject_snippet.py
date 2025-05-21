from pathlib import Path
import os
import re
import sys

# 環境変数からMarkdownファイルのパスを取得
target_md_path = os.environ.get("TARGET_MD")
if not target_md_path:
    print("環境変数 TARGET_MD が設定されていません", file=sys.stderr)
    sys.exit(1)

md_path = Path(target_md_path)
snippet_path = Path("snippets") / f"{md_path.stem}.py" # ← .md → .py に変換して同名スニペットを推定

if not md_path.exists() or not snippet_path.exists():
    print(f"ファイルが見つかりません: {md_path=} {snippet_path=}", file=sys.stderr)
    sys.exit(1)

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
