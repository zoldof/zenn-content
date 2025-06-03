def to_md_output(result: str):
    data = json.loads(result)
    output = "\n".join(f"{key}: {value}" for key, value in data.items())
    return output
