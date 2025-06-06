import sys
from io import StringIO
from unittest.mock import patch
from pathlib import Path
import re

basename = sys.argv[1]
md_path = Path(sys.argv[2])
init_path = Path("tools/init.py")
py_path = Path(sys.argv[3])
measure_path = Path("tools/measure.py")
output_path = Path("tools/output.py")
input_block_id = f"{basename}_in"
output_block_id = f"{basename}_out"

inputs = {
    "hello_01": ["太郎"],
    "time-calc_01": ["10:00:00", "13:00:00"],
}

# 複数ファイルを順に読み込むための準備
files = [init_path, py_path, measure_path, output_path]

# 出力を捕捉するための設定
output = StringIO()
original_stdout = sys.stdout
sys.stdout = output

def load_combined_code(paths):
    combined = ""
    for path in paths:
        with open(path, encoding="utf-8") as f:
            combined += f.read() + "\n"
    return combined

def execute_and_capture(code_str, namespace, *args):
    try:
        exec(code_str, namespace)
        if "to_md_output" in namespace:
            result = namespace["to_md_output"](*args)
            print(result)
        else:
            print("to_md_output 関数が見つかりません。")
    finally:
        sys.stdout = original_stdout

    return output.getvalue()

def replace_multiple_blocks(md_text, replacement_dict):
    pattern = r"```(?P<block_id>[^\n]+)\n(.*?)\n?```"

    def replacer(match):
        block_id = match.group("block_id")
        content = replacement_dict.get(block_id)
        if content is not None:
            return f"```{block_id}\n{content.strip()}\n```"
        return match.group(0)  # 対象外はそのまま残す

    return re.sub(pattern, replacer, md_text, flags=re.DOTALL)

if __name__ == "__main__":
    combined_code = load_combined_code(files)
    replacements = {
        input_block_id: "\n".join(inputs[basename]),
        output_block_id: execute_and_capture(combined_code, {}, *inputs[basename])
    }
    md_text = md_path.read_text(encoding="utf-8")
    md_text = replace_multiple_blocks(md_text, replacements)
    md_path.write_text(md_text, encoding="utf-8")
