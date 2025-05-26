import sys
from io import StringIO
from unittest.mock import patch
from pathlib import Path
import re

basename = sys.argv[1]
md_path = Path(sys.argv[2])
py_path = Path(sys.argv[3])
input_block_id = f"{basename}_in"
output_block_id = f"{basename}_out"

input = "太郎"
# 出力を捕捉するための設定
output = StringIO()
original_stdout = sys.stdout
sys.stdout = output

try:
    namespace = {}
    with open(py_path, encoding="utf-8") as f:
        code = f.read()
        exec(code, namespace)

    if "main" in namespace:
        result = namespace["main"](input)
        print(result)
    else:
        print("main 関数が見つかりません。")

finally:
    sys.stdout = original_stdout

# Markdownファイルを読み込んで、指定ブロックを置き換え
md_text = md_path.read_text(encoding="utf-8")
pattern = rf"```{re.escape(input_block_id)}\n.*?\n```"
replacement = f"```{input_block_id}\n{input}\n```"
new_md = re.sub(pattern, replacement, md_text, flags=re.DOTALL)

pattern = rf"```{re.escape(output_block_id)}\n.*?\n```"
replacement = f"```{output_block_id}\n{output.getvalue().strip()}\n```"
new_md = re.sub(pattern, replacement, md_text, flags=re.DOTALL)

# 上書き保存
md_path.write_text(new_md, encoding="utf-8")
