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

inputs = {
    "hello_01": ["太郎"],
    "time-calc_01": ["10:00:00", "13:00:00"],
}
#input = "太郎"
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
        result = namespace["main"](*inputs[basename])
        print(result)
    else:
        print("main 関数が見つかりません。")

finally:
    sys.stdout = original_stdout

def replace_multiple_blocks(md_text, replacement_dict):
    pattern = r"```(?P<block_id>[^\n]+)\n.*?\n```"

    def replacer(match):
        block_id = match.group("block_id")
        content = replacement_dict.get(block_id)
        if content is not None:
            return f"```{block_id}\n{content.strip()}\n```"
        return match.group(0)  # 対象外はそのまま残す

    return re.sub(pattern, replacer, md_text, flags=re.DOTALL)

replacements = {
    input_block_id: "\n".join(inputs[basename]),
    output_block_id: output.getvalue()
}
md_text = md_path.read_text(encoding="utf-8")
md_text = replace_multiple_blocks(md_text, replacements)
md_path.write_text(md_text, encoding="utf-8")
