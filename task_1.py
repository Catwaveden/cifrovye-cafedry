# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Bus:
    def __init__(self, seats_count: int, occupancy_count: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param seats_count: Количество мест в салоне автобуса
        :param occupancy_count: Количество занятых мест в автобусе, пассажиров

        Примеры:
        >>> bus = Bus(52, 12) # инициализация экземпляра класса
        """

        if not isinstance(seats_count, int): #Проверка данных о количестве мест в автобусе
            raise TypeError("Количество мест в автобусе должно быть типа int")
        if seats_count <= 0:
            raise ValueError("Количество мест в автобусе должно быть положительным числом")
        self.seats_count = seats_count

        if not isinstance(occupancy_count, int): #Проверка данных о количестве занятых мест в автобусе
            raise TypeError("Количество занятых мест в автобусе должно быть int")
        if occupancy_count < 0:
            raise ValueError("Количество занятых мест в автобусе не должно быть отрицательным числом")
        self.occupancy_count = occupancy_count

    def is_empty_bus(self) -> bool:
        """
        Функция которая проверяет пустой ли автобус

        :return: Является ли автобус пустым

        Примеры:
        >>> bus = Bus(52, 0)
        >>> bus.is_empty_bus()
        """
        ...

    def add_passengers_to_bus(self, passengers: int) -> None:
        """
        Добавление пассажиров в автобус.

        :param passengers: Количество добавляемых пассажиров

        :raise ValueError: Если количество пассажиров превышает количество свободных мест в автобусе, то вызываем ошибку

        Примеры:
        >>> bus = Bus(52, 0)
        >>> bus.add_passengers_to_bus(52)
        """
        if not isinstance(passengers, int):
            raise TypeError("Прибавляемое количество пассажиров должно быть типа int")
        if passengers < 0:
            raise ValueError("Прибавляемое количество пассажиров должно быть положительным числом")
        ...

    def remove_passenger_from_bus(self, vacated_seats: int) -> None:
        """
        Освобождение мест автобуса

        :param vacated_seats: Количество освобожденных мест
        :raise ValueError: Если количество освобожденных мест превышает количество занятых мест,
        то возвращается ошибка.

        Примеры:
        >>> bus = Bus(52, 25)
        >>> bus.remove_passenger_from_bus(2)
        """
        ...

        if not isinstance(vacated_seats, int):
            raise TypeError("Количество освобожденных мест должно быть типа int")
        if vacated_seats < 0:
            raise ValueError("Количество освобожденных мест должно быть положительным числом")
        if vacated_seats > self.occupancy_count:
            raise ValueError("Количество освобожденных мест должно быть меньше количества занятых мест автобуса")

        ...

class PiggyBank:
    def __init__(self, piggybank_name: str, piggybank_id: int, money_amount: float):
        """
        Создание и подготовка к работе объекта "Копилка"

        :param piggybank_name: Название копилки, данное пользователем
        :param piggybank_id: Идентификационный номер копилки в банковской системе
        :param money_amount: Количество денег на счете копилки

        Примеры:
        >>> piggybank = PiggyBank("На отпуск", 1234567, 12300.47) # инициализация экземпляра класса
        """
        if not isinstance(piggybank_name, str): #Проверка данных о количестве мест в автобусе
            raise TypeError("Название копилки должно быть типа str")
        if len(piggybank_name) <= 3 or len(piggybank_name) >= 30:
            raise ValueError("Количество символов в названии копилки должно быть от 3 до 30 символов")
        self.piggybank_name = piggybank_name

        if not isinstance(piggybank_id, int): #Проверка данных о количестве мест в автобусе
            raise TypeError("ID копилки должен быть типа int")
        if piggybank_id <= 0:
            raise ValueError("ID копилки должен быть положительным числом")
        self.piggybank_id = piggybank_id

        if not isinstance(money_amount, (int, float)): #Проверка данных о количестве занятых мест в автобусе
            raise TypeError("Сумма денег в копилке должна быть int или float")
        if money_amount < 0:
            raise ValueError("Сумма денег в копилке не должна быть отрицательным числом")
        self.money_amount = money_amount

    def change_piggybank_name(self, new_piggybank_name) -> None:
        """
        Функция которая меняет название копилки

        :param new_piggybank_name: Новое название копилки

        Примеры:
        >>> piggybank = PiggyBank("На отпуск", 1234567, 12300.47)
        >>> piggybank.change_piggybank_name("На машину")
        """
        if len(new_piggybank_name) <= 3 or len(new_piggybank_name) >= 30:
            raise ValueError("Количество символов в названии копилки должно быть от 3 до 30 символов")

        ...


    def add_money_to_piggybank(self, added_money: float) -> None:
        """
        Добавление денег на счет

        :param added_money: Сумма денег, положенных в копилку
        :raise ValueError: Если новое название копилки короче 3 символов или длиннее 30, то возвращается ошибка.

        Примеры:
        >>> piggybank = PiggyBank("На отпуск", 1234567, 12300.47)  # инициализация экземпляра класса
        >>> piggybank.add_money_to_piggybank(2500.25)
        """
        ...

        if not isinstance(added_money, (float, int)):
            raise TypeError("Сумма добавленных денег должна быть типа float или int")
        if added_money <= 0:
            raise ValueError("Сумма добавленных денег должна быть положительным числом")
        ...

    def remove_money_from_piggybank(self, removed_money: float) -> None:
        """
        Снятие денег со счета

        :param removed_money: Сумма денег, вычтенных из копилки
        :raise ValueError: Если сумма вычитаемых денег больше текущего баланса, то возвращается ошибка.

        Примеры:
        >>> piggybank = PiggyBank("На отпуск", 1234567, 12300.47) # инициализация экземпляра класса
        >>> piggybank.remove_money_from_piggybank(2500.25)
        """
        ...

        if not isinstance(removed_money, (int,float)):
            raise TypeError("Сумма снятых со счета копилки денег должна быть типа int или float")
        if removed_money <= 0:
            raise ValueError("Сумма снятых со счета копилки денег должна быть положительным числом")
        if removed_money > self.money_amount:
            raise ValueError("Сумма денег, снятых со счета копилки должна быть меньше текущего баланса")
        ...

    def how_much_until_goal(self, goal: float) -> float:
        """
        Возвращает сколько денег не хватает для оплаты той или иной цели.

        :param goal: Сумма денег, которой не хватает для оплаты той или иной цели.

        :return сумма денег, которой не хватает для оплаты той или иной цели self.money_amount - goal, float

        Примеры:
        >>> piggybank = PiggyBank("На отпуск", 1234567, 12300.47) # инициализация экземпляра класса
        >>> piggybank.remove_money_from_piggybank(2500.25)
        """
        ...

        if not isinstance(goal, (int,float)):
            raise TypeError("Сумма снятых со счета копилки денег должна быть типа int или float")
        if goal <= 0:
            raise ValueError("Сумма снятых со счета копилки денег должна быть положительным числом")
        ...

class Street:
    def __init__(self, street_name: str, street_houses: list[int], street_length: float):
        """
        Создание и подготовка к работе объекта "Улица"

        :param street_name: Название улицы
        :param street_houses: Номера домов на улице
        :param street_length: Длина улицы в метрах

        Примеры:
        >>> street = Street("Политехническая улица", [1, 2, 3, 5, 7, 8], 2986.4) # инициализация экземпляра класса
        """
        if not isinstance(street_name, str): #Проверка данных о названии улицы
            raise TypeError("Название улицы должно быть типа str")
        self.street_name = street_name

        if not isinstance(street_houses, list): #Проверка данных о списке номеров домов на улице
            raise TypeError("Список номеров домов на улице должен быть типа list")
        for number in street_houses:
            if not isinstance(number, int):
                raise TypeError("Номера домов в списке номеров домов на улице должны быть типа int")
            if number <= 0:
                raise ValueError("Номера домов в списке номеров домов на улице должны быть положительным числом")
        self.street_houses = street_houses

        if not isinstance(street_length, (int, float)): #Проверка данных о количестве занятых мест в автобусе
            raise TypeError("Длина улицы должна быть int или float")
        if street_length <= 0:
            raise ValueError("Длина улицы должна быть положительным числом")
        self.street_length = street_length

    def change_street_name(self, new_street_name) -> None:
        """
        Функция которая меняет название улицы

        :param new_street_name: Новое название улицы

        Примеры:
        >>> street = Street("Политехническая улица", [1, 2, 3, 5, 7, 8], 2986.4)
        >>> street.change_street_name("Горная улица")
        """
        ...

    def add_house_number(self, house_number: int) -> None:
        """
        Добавление нового дома к списку домов

        :param house_number: Номер нового дома
        :raise ValueError: Если номер уже есть в списке номеров, возвращается ошибка

        Примеры:
        >>> street = Street("Политехническая улица", [1, 2, 3, 5, 7, 8], 2986.4) # инициализация экземпляра класса
        >>> street.add_house_number(4)
        """
        ...

        if not isinstance(house_number, int):
            raise TypeError("Номер дома должен быть типа int")
        if house_number <= 0:
            raise ValueError("Номер дома должен быть положительным числом")
        if house_number in self.street_houses:
            raise ValueError("Номер дома не должен присутствовать в списке номеров")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
