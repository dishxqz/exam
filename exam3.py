import re
import random
from enum import Enum

#3
class status_of_work(Enum):
    DONE = 'выполнен'
    PROCESS = 'осуществляется'
    PLANNED = 'запланирован'
    ERROR = 'забракован'
class Stage:
    def __init__(self, cost, time_of_start, time_of_ending, description, status):
        self.__cost = cost
        self.__time_of_start = time_of_start
        self.__time_of_ending = time_of_ending
        self.description = description
        self.__status = status

    def getDetails(self):
        return (f'Цена: {self.__cost}, начало стройки: {self.__time_of_start}, конец стройки: {self.__time_of_ending}, описание: {self.description}, статус: {self.__status}')

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if not isinstance(cost, int) or cost <= 0:
            raise TypeError('Введите пололжительное число')
        self.__cost = cost

    @property
    def time_of_start(self):
        return self.__time_of_start

    @time_of_start.setter
    def time_of_start(self, time_of_start):
        if not re.match(r'[0-3]\d\.[0-1]\d\.\d{4}', time_of_start):
            raise TypeError("Введите в формате дд.мм.гггг")
        self.__time_of_start = time_of_start

    @property
    def time_of_ending(self):
        return self.__time_of_ending

    @time_of_ending.setter
    def time_of_ending(self, time_of_ending):
        if not re.match(r'[0-3]\d\.[0-1]\d\.\d{4}', time_of_ending):
            raise TypeError("Введите в формате дд.мм.гггг")
        self.__time_of_ending = time_of_ending

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if not status in status_of_work:
            raise TypeError("Введите этап")
        self.__status

    def next(self):
        if self.__status == 'осуществляется':
            self.__status = 'выполнен'
        if self.__status == 'запланирован':
            self.__status = 'осуществляется'
        if self.__status == 'забракован':
            raise TypeError("Все уже, брак")
        if self.__status == 'выполнен':
            raise TypeError('Дальше некуда')

    def prev(self):
        if self.__status == 'выполнен':
            self.__status = 'осуществляется'
        if self.__status == 'осуществляется':
            self.__status = 'запланирован'
        if self.__status == 'забракован':
            raise TypeError("Все уже, брак")
        if self.__status == 'запланирован':
            raise TypeError('Назад некуда')

    def start(self):
        self.description = "Стройка начата"
        print(self.description)

    def stop(self):
        self.description = 'Стройка приостановлена'
        print(self.description)

    def brack(self):
        self.__status = 'забракован'
        print('Объект забракован')

class Project(Stage):
    def init(self, cost, time_of_start, time_of_ending, description, status):
        super().__init__(cost, time_of_start, time_of_ending, description, status)

class Foundation(Stage):
    def init(self, cost, time_of_start, time_of_ending, description, status):
        super().__init__(cost, time_of_start, time_of_ending, description, status)

class Walls(Stage):
    def init(self, cost, time_of_start, time_of_ending, description, status):
        super().__init__(cost, time_of_start, time_of_ending, description, status)

class Roof(Stage):
    def init(self, cost, time_of_start, time_of_ending, description, status):
        super().__init__(cost, time_of_start, time_of_ending, description, status)

class Electricity(Stage):
    def init(self, cost, time_of_start, time_of_ending, description, status):
        super().__init__(cost, time_of_start, time_of_ending, description, status)

class Finishing(Stage):
    def __init__(self, cost, time_of_start, time_of_ending, description, status):
        super().__init__(cost, time_of_start, time_of_ending, description, status)

class Construction:
    def __init__(self, time_of_start, time_of_ending):
        self.__time_of_start = time_of_start
        self.__time_of_ending = time_of_ending
        self.stages = []

    @property
    def time_of_start(self):
        return self.__time_of_start

    @time_of_start.setter
    def time_of_start(self, time_of_start):
        if not re.match(r'[0-3]\d\.[0-1]\d\.\d{4}', time_of_start):
            raise TypeError("Введите в формате дд.мм.гггг")
        self.__time_of_start = time_of_start

    @property
    def time_of_ending(self):
        return self.__time_of_ending

    @time_of_ending.setter
    def time_of_ending(self, time_of_ending):
        if not re.match(r'[0-3]\d\.[0-1]\d\.\d{4}', time_of_ending):
            raise TypeError("Введите в формате дд.мм.гггг")
        self.__time_of_ending = time_of_ending

    def run(self):
        choices = ['удалось', "не удалось"]
        return random.choice(choices)

    def start_construct(self):
        return random.choices(['удалось', 'не удалось'], weights=[90, 10])

