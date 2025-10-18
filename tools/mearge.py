#**********
#init.py
#**********

#モジュール
##初期データ用
###import random

##測定用
import time, tracemalloc

##各種アルゴリズム共通簡略化
###from datetime import timedelta

##出力用
import json

#データ作成
###n = 1000
###min_val = 0
###max_val = 999
###data = [random.randint(min_val, max_val) for _ in range(n)]

#**********
#measure.py
#**********

def measure(*args):
    tracemalloc.start()
    start_time = time.perf_counter()

    result = main(*args) 

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed_time = end_time - start_time
    
    result_data = {
        "実行時間　　　　": f"{elapsed_time:.6f} 秒",
        "メモリ（現時点）": f"{current} bytes",
        "メモリ（ピーク）": f"{peak} bytes",
        "実行結果　　　　": f"{result}"
    }

    json_str = json.dumps(result_data, ensure_ascii=False)
    return json_str

#**********
#output.py
#**********

def to_md_output(*arg):
    result = measure(*arg)
    data = json.loads(result)
    output = "\n".join(f"{key}: {value}" for key, value in data.items())
    return output
