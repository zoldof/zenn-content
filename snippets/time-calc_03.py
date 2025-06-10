#簡略化
##timedeltaでfrom_seconds関数を代替する
##dateutillやpandasでも動作する
def calc_datetime(start_str, end_str):
    from datetime import datetime
    fmt = "%H:%M:%S"
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    diff = end - start 
    if diff.total_seconds() < 0:
        diff += timedelta(days=1)
    return str(diff)
