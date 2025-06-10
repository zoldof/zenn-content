##共通の関数
def from_seconds(total_seconds):
    if total_seconds < 0:
        total_seconds += 24 * 3600
    total_seconds = int(total_seconds)
    h = total_seconds // 3600
    total_seconds %= 3600
    m = total_seconds // 60
    s = total_seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

#標準
def calc_datetime_01(start_str, end_str):
    from datetime import datetime
    fmt = "%H:%M:%S"
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    diff = end - start 
    return from_seconds(diff.total_seconds())

#拡張
def calc_dateutil(start_str, end_str):
    from dateutil import parser
    start = parser.parse(start_str)
    end = parser.parse(end_str)
    diff = end - start
    return from_seconds(diff.total_seconds())

def calc_pandas(start_str, end_str):
    import pandas as pd
    start = pd.Timestamp(start_str)
    end = pd.Timestamp(end_str)
    diff = end - start
    return from_seconds(diff.total_seconds())

#簡略化
def calc_datetime_02(start_str, end_str):
    from datetime import datetime
    fmt = "%H:%M:%S"
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    diff = end - start 
    #timedeltaでfrom_seconds関数を代替する
    #dateutillやpandasでも動作する
    if diff.total_seconds() < 0:
        diff += timedelta(days=1)
    return str(diff)
