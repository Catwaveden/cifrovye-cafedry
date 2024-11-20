import json

FILENAME = "input.json"


# TODO решите задачу

def task() -> float:
    with open(FILENAME) as input_file:
        json_data = json.load(input_file)
    total_multiplication_sum = sum([item["score"] * item["weight"] for item in json_data])
    return round(total_multiplication_sum, 3)

print(task())
