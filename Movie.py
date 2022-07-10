from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        generator = []
        for el in self.dates:
            date = el[0]
            while date <= el[1]:
                generator.append(date)
                date += timedelta(days=1)
        return generator


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

print(m.dates)

for d in m.schedule():
    print(d)
