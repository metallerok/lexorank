from dataclasses import dataclass
from src.lexorank import get_rank


@dataclass
class Item:
    title: str
    rank: str


def test_get_rank():
    rank = get_rank(next_rank="cccadskljfadsfas")

    print(rank)
