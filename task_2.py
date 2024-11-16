# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    # TODO считать содержимое csv файла

    indent = 4
    ensure_ascii = True
    delimiter = ","
    newline = "\n"

    with open(INPUT_FILENAME, "r", newline = newline) as csv_file:
        csv_file_data = csv.DictReader(csv_file, delimiter=delimiter)
        to_json_items = [row for row in csv_file_data]

    # TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(to_json_items, json_file, indent=indent, ensure_ascii=ensure_ascii)

    return

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
