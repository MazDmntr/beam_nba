
def json_to_csv_line(element):
    line_csv = [str(value) if not isinstance(value, dict) else json_to_csv_line(value) for value in element.values()]
    return ",".join(line_csv).replace(",,", ",")