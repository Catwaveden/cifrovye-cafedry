import json

FILENAME = "input.json"


# TODO решите задачу

def task() -> float:
    with open(FILENAME) as input_file:
        json_data = json.load(input_file)
    total_multiplication_sum = 0
    for item in json_data:
        total_multiplication_sum += item["score"] * item["weight"]
    return round(total_multiplication_sum, 3)

print(task())

