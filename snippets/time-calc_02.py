# 標準
def calc_datetime(start_str, end_str):
    fmt = "%H:%M:%S"
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    diff = end - start 
    if diff.total_seconds() < 0:
        diff += timedelta(days=1)
    return str(diff)  # 例: '0:30:00'

# 拡張
def calc_dateutil(start_str, end_str, tz_str='UTC'):
    tz = pytz.timezone(tz_str)
    start = tz.localize(parser.parse(start_str))
    end = tz.localize(parser.parse(end_str))
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
    start = pd.Timestamp(start_str)
    end = pd.Timestamp(end_str)
    diff = end - start  # 常に正の差分にする
    if diff.total_seconds() < 0:
        diff += pd.Timedelta('1 day')  # 時計回りに補正
    total_seconds = int(diff.total_seconds())
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02}:{m:02}:{s:02}"
    
