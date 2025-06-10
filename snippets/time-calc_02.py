#標準
def calc_datetime(start_str, end_str):
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
