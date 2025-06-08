from datetime import datetime

def main(t1: str, t2: str) -> str:
    fmt = "%H:%M:%S"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    diff = abs(dt1 - dt2)
    return str(diff)  # '1:15:00' のような文字列
