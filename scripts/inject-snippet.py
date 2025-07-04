from pathlib import Path
import re
import sys

basename = sys.argv[1]
md_path = Path(sys.argv[2])
base_stem = basename.split('_')[0]

# snippets/foo_1.py, foo_2.py, ... を探す
snippet_files = sorted(Path("snippets").glob(f"{base_stem}_*.py"))

if not md_path.exists() or not snippet_files:
    print(f"ファイルが見つかりません: {md_path=} {snippet_files=}", file=sys.stderr)
    sys.exit(1)

with md_path.open() as f:
    content = f.read()

# 各コードブロックに順番に挿入
def replace_nth_code_block(content, codes):
    pattern = r'```python\n(.*?)\n?```'
    matches = list(re.finditer(pattern, content, flags=re.DOTALL))
    if len(codes) != len(matches):
        print(f"警告: コードブロック数 {len(matches)} とスニペット数 {len(codes)} が一致しません", file=sys.stderr)

    result = []
    last_index = 0

    for match, code in zip(matches, codes):
        start, end = match.span()
        result.append(content[last_index:start])  # 前の部分
        result.append(f'```python\n{code.strip()}\n```') # 差し替えコード
        last_index = end

    result.append(content[last_index:])  # 残りの部分を追加
    return ''.join(result)

# スニペット読み込み
codes = [f.read_text() for f in snippet_files]

# Markdown更新
new_content = replace_nth_code_block(content, codes)
md_path.write_text(new_content)
