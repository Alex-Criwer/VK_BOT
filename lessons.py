from commands import WEEK
from datetime import time, datetime, timedelta, date


class lesson:
    def __init__(self, name, time_begin, time_end, classroom):
        self.name = name
        self.time_begin = time_begin
        self.time_end = time_end
        self.classroom = classroom

lessons = { WEEK.MONDAY: [],
            WEEK.TUESDAY:
                [lesson(name='ТПМС',             time_begin=time(10, 45), time_end=(12, 10), classroom='УЛК-2, №425'),
                 lesson(name='Теорвер',          time_begin=time(12, 20), time_end=(13, 45), classroom='ГК 516'),
                 lesson(name='Иностранный язык', time_begin=time(13, 55), time_end=(15, 20), classroom='НК')],
            WEEK.WEDNESDAY:
                [lesson(name='Аналмех',          time_begin=time(10, 45), time_end=(12, 10), classroom='ГК 123'),
                 lesson(name='БД',               time_begin=time(15, 30), time_end=(16, 55), classroom='УЛК-2, №418'),
                 lesson(name='Общефиз',          time_begin=time(17, 5),  time_end=(18, 30), classroom='ГК 515')],
            WEEK.THURSDAY:
                [lesson(name='Матан лекция',     time_begin=time(9, 00),  time_end=(10, 25), classroom='202 НК'),
                 lesson(name='Аналмех лекция',   time_begin=time(10, 45), time_end=(12, 10), classroom='113 ГК'),
                 lesson(name='Физика лекция',    time_begin=time(12, 20), time_end=(13, 45), classroom='гл. Физ')],
            WEEK.FRIDAY:
                [lesson(name='Матан Орел',       time_begin=time(10, 45), time_end=(12, 10), classroom='УЛК-2, №425'),
                 lesson(name='Диффуры',          time_begin=time(12, 20), time_end=(13, 45), classroom='дистант'),
                 lesson(name='Иностранный язык', time_begin=time(13, 55), time_end=(15, 20), classroom='НК'),
                 lesson(name='Лабы',             time_begin=time(15, 30), time_end=(18, 30), classroom='ГК')],
            WEEK.SUNDAY:
                [lesson(name='Диффуры лекция',   time_begin=time(9, 00),  time_end=(10, 25), classroom='дистант'),
                 lesson(name='Теорвер лекция',   time_begin=time(10, 45), time_end=(12, 10), classroom='дистант'),
                 lesson(name='ТПМС лекция',      time_begin=time(12, 20), time_end=(13, 45), classroom='УЛК-2'),
                 lesson(name='БД лекция',        time_begin=time(13, 55), time_end=(15, 20), classroom='дистант')],
            WEEK.SATURDAY: []}
