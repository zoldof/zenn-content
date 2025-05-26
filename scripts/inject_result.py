import sys
from io import StringIO
from unittest.mock import patch

md_path = sys.argv[1]
py_path = sys.argv[2]

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
        result = namespace["main"]("太郎")
        print(result)
    else:
        print("main 関数が見つかりません。")

finally:
    sys.stdout = original_stdout

# .md に追記
with open(md_path, "a", encoding="utf-8") as f:
    f.write("\n---\n\n### 実行結果\n\n```text\n")
    f.write(output.getvalue().strip())
    f.write("\n```\n")
