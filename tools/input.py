if __name__ == "__main__":    
    # ▼ 時刻差分のアルゴリズム
    try:
        start = input("開始時刻を入力してください（hh:mm:ss）: ")
        end = input("終了時刻を入力してください（hh:mm:ss）: ")
        args = [start, end]
    except ValueError as ve:
        print("エラー:", ve)
    except Exception:
        print("入力形式が正しくありません。hh:mm:ss で入力してください。")
    '''
    この記号で囲うとコメントアウトできます
    '''
    
    # ▼ 並べ替えのアルゴリズム
    # args = [date]

    # ▼ 共通の実行部分
    print_result(output(*args))
