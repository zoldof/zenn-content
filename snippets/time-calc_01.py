#test
def parse_time(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h, m, s

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def from_seconds(total_seconds):
    h = total_seconds // 3600
    total_seconds %= 3600
    m = total_seconds // 60
    s = total_seconds % 60
    return h, m, s

def format_time(h, m, s):
    return f"{h:02}:{m:02}:{s:02}"

def main(start, end):
    h1, m1, s1 = parse_time(start)
    h2, m2, s2 = parse_time(end)
    
    sec1 = to_seconds(h1, m1, s1)
    sec2 = to_seconds(h2, m2, s2)

    if sec2 < sec1:
        sec2 += 24 * 3600  # 翌日とみなす

    diff = sec2 - sec1
    h, m, s = from_seconds(diff)
    return format_time(h, m, s)
