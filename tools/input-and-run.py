# ▼ 時刻差分のアルゴリズムの入力エラーチェック関数_1
def parse_time_input(input_str):
    parts = input_str.split(":")
    if len(parts) != 3 or not all(part.isdigit() and len(part) == 2 for part in parts):
        raise ValueError("時刻は hh:mm:ss の形式で2桁ずつ入力してください（例：08:30:00）。")

    h, m, s = map(int, parts)

    if not (
        (0 <= h <= 23 or (h == 24 and m == 0 and s == 0)) and
        (0 <= m < 60) and
        (0 <= s < 60)
    ):
        raise ValueError("無効な時刻です。時は 0–23、または 24:00:00 のみ有効です。")

    return input_str

# ▼ 時刻差分のアルゴリズムの入力エラーチェック関数_2
def validate_start_end(start_str, end_str):
    if start_str == end_str:
        raise ValueError("開始時刻と終了時刻が同じです。異なる時刻を入力してください。")
    
def input_and_run():
    # ▼ 時刻差分のアルゴリズム
    try:
        print("開始時刻を入力してください（hh:mm:ss）: ")
        start = parse_time_input(input())
        print("終了時刻を入力してください（hh:mm:ss）: ")
        end = parse_time_input(input())
        validate_start_end(start, end)
        
        print("\n--- 入力確認 ---")
        print(f"開始時刻: {start}")
        print(f"終了時刻: {end}")
        print("→ 入力は正常です。")
    except ValueError as ve:
        print("エラー:", ve)
        return
    except EOFError:
        print("入力が終了されました（EOF）。プログラムを終了します。")
        return
    except KeyboardInterrupt:
        print("\n入力がキャンセルされました（Ctrl+C）。プログラムを終了します。")
        return
    except Exception as e:
        print("予期しないエラーが発生しました:", e)
        return
        
    args = [start, end]
    
    # ▼ 並べ替えのアルゴリズム
    # args = date

    # ▼ 共通の実行部分
    print("\n--- 出力確認 ---")
    print(f"{to_md_output(*args)}")
    
if __name__ == "__main__": 
    input_and_run()
