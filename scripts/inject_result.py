from pathlib import Path
import os
import re
import sys
import subprocess

# 環境変数からMarkdownファイルのパスを取得
target_md_path = os.environ.get("TARGET_MD")
if not target_md_path:
    print("環境変数 TARGET_MD が設定されていません", file=sys.stderr)
    sys.exit(1)

def get_input_text(input_type: str) -> str | None:
    """対応する入力データを取得（あらかじめ定義しておく）"""
    predefined_inputs = {
        "hello_01": "Alice\n",
        "time-culc": "12:00:00\n14:30:00\n",
    }
    return predefined_inputs.get(input_type)

def run_python_file(py_path: Path, input_text: str = None) -> str:
    """Pythonファイルを実行し、出力を取得"""
    if input_text:
        result = subprocess.run(
            ['python', str(py_path)],
            input=input_text.encode(),
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(
            ['python', str(py_path)],
            capture_output=True,
            text=True
        )
    return result.stdout.strip()

def update_markdown(md_path: Path, output: str, input_type: str):
    """マークダウン内のoutput_xxブロックを置換"""
    md_text = md_path.read_text(encoding='utf-8')
    block_start = f"```{input_type}"
    block_end = "```"

    pattern = re.compile(
        f"{re.escape(block_start)}.*?{re.escape(block_end)}",
        re.DOTALL
    )
    new_block = f"{block_start}\n{output}\n{block_end}"
    md_text = pattern.sub(new_block, md_text)

    md_path.write_text(md_text, encoding='utf-8')

def main():
    src_dir = Path("src")
    md_dir = Path(target_md_path)
    md_path = Path()

    for py_file in src_dir.glob("*.py"):
        input_type = extract_input_type(py_file)
        input_text = get_input_text(input_type) if input_type else None
        output = run_python_file(py_file, input_text)

        md_path = md_dir / (py_file.stem.split("_")[0] + ".md")
        if not md_path.exists():
            print(f"スキップ: {md_path.name}（Markdownファイルが見つかりません）")
            continue

        update_markdown(md_path, output, input_type)
        print(f"{py_file.name} の出力を {md_path.name} に反映しました。")
