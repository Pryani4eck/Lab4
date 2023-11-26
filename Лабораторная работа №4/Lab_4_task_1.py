# TODO решите задачу
import json
def task() -> float:
    name = "input.json"
    with open(name) as f:
        json_data = json.load(f)

    calculate = sum([item["score"] * item["weight"] for item in json_data])
    return round(calculate, 3)

print(task())