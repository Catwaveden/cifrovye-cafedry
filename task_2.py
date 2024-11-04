# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ","):
    first_group_participants = set(first_group.split(sep = separator))
    second_group_participants = second_group.split(sep = separator)

    common_participants = first_group_participants.intersection(second_group_participants)

    common_participants_formated = list(common_participants)
    common_participants_formated.sort()

    return common_participants_formated

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))