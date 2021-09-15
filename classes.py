from dataclasses import dataclass
from enum import Enum
from typing import Optional, Callable


class E(Enum):
    ZERO = 0
    ONE = 1


@dataclass
class Strand:
    value: float
    next_tassel: Optional['Tassel'] = None


@dataclass
class Tassel:
    func: Callable[[E], Strand]

    def __iter__(self):
        for e in E:
            s = self.func(e)

            if s.next_tassel is None:
                yield s.value
            else:
                for value in s.next_tassel:
                    yield s.value + value
