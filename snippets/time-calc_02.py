#標準
def calc_datetime(start_str, end_str):
    from datetime import datetime
    fmt = "%H:%M:%S"
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    diff = end - start 
    
    total_seconds = diff.total_seconds()
    if total_seconds < 0:
        total_seconds += 24 * 3600  # 24時間分を秒で足す
    total_seconds = int(total_seconds)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

#拡張
def dateutil(start_str, end_str):
    from datetime import datetime
    fmt = "%H:%M:%S"
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    diff = end - start 
    
    if diff.total_seconds() < 0:
        diff += timedelta(days=1)
    return str(diff)  # 例: '0:30:00'

#拡張
def calc_dateutil(start_str, end_str):
    from dateutil import parser
    start = parser.parse(start_str)
    end = parser.parse(end_str)
    diff = end - start
    
    total_seconds = diff.total_seconds()
    if total_seconds < 0:
        total_seconds += 24 * 3600  # 24時間分を秒で足す
    total_seconds = int(total_seconds)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def calc_pandas(start_str, end_str):
    import pandas as pd
    start = pd.Timestamp(start_str)
    end = pd.Timestamp(end_str)
    diff = end - start  # 常に正の差分にする
    
    total_seconds = diff.total_seconds()
    if total_seconds < 0:
        total_seconds += 24 * 3600  # 24時間分を秒で足す
    total_seconds = int(total_seconds)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02}:{m:02}:{s:02}"
