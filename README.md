# ylab-third-week-secondtask


1. Задача на циклический итератор. Секция статьи "1. Задача на циклический итератор."
Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.), и когда достигнет последнего элемента, начинать сначала.

cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)

Скопировать
Основа:

class CyclicIterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass
        
       
2. Задача на разжатие массива. Секция статьи "2. Задача на разжатие массива."
У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. Для эффективности дни проката хранятся периодами дат. Например, прокат фильма проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля:

[
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
]

Скопировать
Вам дан class Movie. Реализуйте у него метод schedule. Он будет генерировать дни, в которые показывают фильм.

Основа:

from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return []


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
