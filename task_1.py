class Building:
    """
    Класс Building описывает здание.

    Аргументы:
        length - длина здания
        width - ширина здания
        height - высота здания
        storeys - количество этажей в здании
        roof_type - тип крыши здания

    Методы:
        get_storey_height() - позволяет узнать высоту одного этажа здания
        build_storeys(storey_count) - позволяет пристроить к зданию n (= storey_count) этажей,
            добавить высоту пристроенных этажей к общей высоте здания,
            добавить кол-во пристроенных этажей к общему количеству этожей здания.
    """
    def __init__(self, length: float, width: float, height: float, storeys: int, roof_type: str):
        self.length = length
        self.width = width
        self.height = height
        self.storeys = storeys
        self.roof_type = roof_type

    def __str__(self):
        return f"Здание размером {self.length}м x {self.width}м x {self.height}м. Количество этажей - {self.storeys}. Тип крыши - {self.roof_type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length!r}, width={self.width!r}, height={self.height!r}, storeys={self.storeys!r}, roof_type={self.roof_type!r})"



    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, new_length: float) -> None:
        """
        Длина здания не может быть отрицательный или равной нулю,
        поэтому внутри сеттера проводим проверки, прежде чем установить длину.
        Длина округляется до 2 знаков после запятой.

        :param new_length:
        :return:
        """
        if not(isinstance(new_length, float)):
            raise TypeError("Длина здания должна быть типа float")
        elif new_length <= 0:
            raise ValueError("Длина здания должна быть положительной")
        else:
            self._length = round(new_length, 2)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, new_width: float) -> None:
        """
        Ширина здания не может быть отрицательный или равной нулю,
        поэтому внутри сеттера проводим проверки, прежде чем установить ширину.
        Ширина округляется до 2 знаков после запятой.

        :param new_width:
        :return:
        """
        if not (isinstance(new_width, float)):
            raise TypeError("Ширина здания должна быть типа float")
        elif new_width <= 0:
            raise ValueError("Ширина здания должна быть положительной")
        else:
            self._width = round(new_width, 2)


    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        """
        Высота здания не может быть отрицательный или равной нулю,
        поэтому внутри сеттера проводим проверки, прежде чем установить высоту.
        Высота округляется до 2 знаков после запятой.

        :param new_height:
        :return:
        """
        if not (isinstance(new_height, float)):
            raise TypeError("Высота здания должна быть типа float")
        elif new_height <= 0:
            raise ValueError("Высота здания должна быть положительной")
        else:
            self._height = round(new_height, 2)

    @property
    def storeys(self) -> float:
        return self._storeys

    @storeys.setter
    def storeys(self, new_storeys: int) -> None:
        """
        Кол-во этажей не может быть отрицательным или равным нулю,
        поэтому внутри сеттера проводим проверки,
        прежде чем установить кол-во этаже.

        :param new_storeys:
        :return:
        """
        if not (isinstance(new_storeys, int)):
            raise TypeError("Количество этажей должно быть типа int")
        elif new_storeys <= 0:
            raise ValueError("Количество этажей должно быть положительным")
        else:
            self._storeys = new_storeys



    def get_storey_height(self) -> float:
        """
        Метод get_storey_height возвращает высоту одного этажа здания
        :return:
        """
        return self._height / self._storeys

    def build_storeys(self, storey_count: int) -> None:
        """
        Метод build_storeys(storey_count) прибавляет к высоте здания
        высоту надстроенных этажей (storeys_count * высота этажа), прибавляет к кол-ву
        этажей здания кол-во надстроенных этажей (storey_count).

        :param storey_count:
        :return:
        """
        if not(isinstance(storey_count, int)):
            raise TypeError('Количество достроенных этажей должно быть типа int')
        elif storey_count <= 0:
            raise ValueError("Количество достроенных этажей должно быть больше 0")
        else:
            self._height = round((self._height + self.get_storey_height() * storey_count), 2)
            self._storeys = self._storeys + storey_count



class Warehouse(Building):
    """
    Класс Building описывает здание.

    Аргументы:
        length - длина здания
        width - ширина здания
        height - высота здания
        storeys - количество этажей в здании
        roof_type - тип крыши здания
        business_name - название компании

    Методы:
        get_storey_height() - позволяет узнать высоту одного этажа здания
        build_storeys(storey_count) - позволяет пристроить к зданию n (= storey_count) этажей,
            добавить высоту пристроенных этажей к общей высоте здания,
            добавить кол-во пристроенных этажей к общему количеству этожей здания.
        get_parking_lot_size() - позволяет узнать площадь парковки для здания.
    """


    def __init__(self, length: float, width: float, height: float, storeys: int, roof_type: str, business_name: str):
        super().__init__(length, width, height, storeys, roof_type)
        self.business_name = business_name


    def __str__(self):
        """
        Перегружаем магический метод __str__, унаследованный от класса Building,
        так как у класса Warehouse есть еще атрибут business_name.
        :return:
        """
        return f"Складское здание размером {self.length}м x {self.width}м x {self.height}м. Количество этажей - {self.storeys}. Тип крыши - {self.roof_type}. Компания - {self.business_name}"

    def __repr__(self):
        """
        Перегружаем магический метод __repr__, унаследованный от класса Building,
        так как у класса Warehouse есть еще атрибут business_name.
        :return:
        """
        return f"{self.__class__.__name__}(length={self.length!r}, width={self.width!r}, height={self.height!r}, storeys={self.storeys!r}, roof_type={self.roof_type!r}, business_name={self.business_name!r})"



    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        """
        Высота здания не может быть отрицательный или равной нулю, а также
        не может превышать 40 метров согласно ГОСТу (предположим),
        поэтому внутри сеттера проводим проверки, прежде чем установить высоту.
        Высота округляется до 2 знаков после запятой.

        :param new_height:
        :return:
        """
        if not (isinstance(new_height, float)):
            raise TypeError("Высота складского здания должна быть типа float")
        elif new_height <= 8:
            raise ValueError("Высота складского здания должна быть не менее 8 метров")
        elif new_height >= 40:
            raise ValueError("Высота складского здания должна быть не более 40 метров")
        else:
            self._height = round(new_height, 2)


    def build_storeys(self, storey_count: int)->None:
        """
        Перегружаем метод build_storeys, так как складские здания
        такого типа нельзя строить выше 40 метров. (предположим).
        Теперь метод build_storeys проверяет тип storey_count,
        кол-ва надстроенных этажей, и следит, чтобы общая высота не превышала 40м

        :param storey_count:
        :return:
        """
        new_building_height = self._height + self.get_storey_height() * storey_count
        if not(isinstance(storey_count, int)):
            raise TypeError('Количество достроенных этажей должно быть типа int')
        elif storey_count <= 0:
            raise ValueError("Количество достроенных этажей должно быть больше 0")
        elif new_building_height > 40:
            raise ValueError("Общая высота здания с надстроенными этажами не должна превышать 40 метров")
        else:
            self._height = round(new_building_height, 2)
            self._storeys = self._storeys + storey_count


    def get_parking_lot_size(self) -> float:
        """
        Метод get_parking_lot_size возвращает общую площадь в м^2, которую компания
        при постройке склада обязана выделить под парковку.

        Предположим, что согласно ограничениям для коммерческого здания
        площадью меньше 100000м^2 требуется 4 парковочных места
        на 100м^2 рабочей области склада, а для зданий больше 100000м^2
        - 6 парковочных мест на 100м^2 рабочей области склада.

        :return:
        """
        PARKING_SPACE = 12.5
        if self.length * self.width * self.storeys < 100000:
            parking_allowance = 4
        else:
            parking_allowance = 6
        return round(PARKING_SPACE * parking_allowance)


if __name__ == "__main__":
    # Write your solution here

    # Создаем экземпляр класса Building
    building1 = Building(25.5, 15.8, 24.3, 9, 'flat')

    # Выводим представление экземпляра класса __str__
    print(building1)
    # Выводим представление экземпляра класса __repr__
    print(repr(building1))

    # Выводим высоту одного этажа здания
    print(building1.get_storey_height())

    # Надстраиваем 3 этажа над зданием, увеличиваем его высоту и кол-во этажей
    building1.build_storeys(3)
    print(building1)



    # Создаем экземпляр класса Warehouse
    warehouse = Warehouse(56.7, 15.8, 16.2, 2, 'flat', 'Amazon')

    # Выводим представление экземпляра класса __str__
    print(warehouse)
    # Выводим представление экземпляра класса __repr__
    print(repr(warehouse))

    # Надстраиваем 2 этажа над складом, увеличиваем его высоту и кол-во этажей
    warehouse.build_storeys(2)
    print(warehouse)

    # Выводим требуемую площадь парковки склада
    print(warehouse.get_parking_lot_size())

    # Надстраиваем 22 этажа над складом, увеличиваем его высоту и кол-во этажей
    # Получаем ошибку, так как высота склада не должна превышать 40м.
    warehouse.build_storeys(22)
    print(warehouse)



