#
def to_md_output(*arg):
    result = measure(*arg)
    data = json.loads(result)
    output = "\n".join(f"{key}: {value}" for key, value in data.items())
    return output
