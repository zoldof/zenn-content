# scripts/inject_result.py

import sys
import builtins
from io import StringIO
from unittest.mock import patch

md_path = sys.argv[1]
py_path = sys.argv[2]

# 出力をキャプチャ
output = StringIO()
sys.stdout = output

# input() のモック
with patch('builtins.input', return_value='太郎'):
    exec(open(py_path).read(), {})

# 出力取得と戻す
sys.stdout = sys.__stdout__
result = output.getvalue()

# Markdown に追記
with open(md_path, "a") as f:
    f.write("\n---\n\n### 実行結果\n\n```text\n")
    f.write(result)
    f.write("```\n")
