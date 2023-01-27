import math
from typing import List, Tuple

ALPHABET_SIZE = 26
MIN_VALUE = "aaa"
MAX_VALUE = "zzz"


def get_rank(prev_rank: str = MIN_VALUE, next_rank: str = MAX_VALUE) -> str:
    if prev_rank > next_rank:
        raise ValueError("Prev rank must be lower than next rank")

    prev_rank, next_rank = _make_ranks_length_equal(prev_rank, next_rank)

    prev_rank_codes = _get_rank_codes(prev_rank)
    next_rank_codes = _get_rank_codes(next_rank)

    difference: int = 0
    index = len(prev_rank_codes) - 1

    while index >= 0:
        prev_code = prev_rank_codes[index]
        next_code = next_rank_codes[index]

        if next_code < prev_code:
            next_code += ALPHABET_SIZE
            next_rank_codes[index - 1] -= 1

        pow_res = math.pow(ALPHABET_SIZE, len(prev_rank) - index - 1)
        difference += (next_code - prev_code) * pow_res

        index -= 1

    rank = ""

    if difference <= 1:
        rank += prev_rank + chr(ord("a") + ALPHABET_SIZE // 2)
    else:
        difference = difference // 2

        offset = 0
        index = 0

        while index < len(prev_rank):
            index += 1
            diff_in_symbols = difference // math.pow(ALPHABET_SIZE, index) % ALPHABET_SIZE
            new_rank_code = int(ord(prev_rank[len(next_rank) - index - 1]) + diff_in_symbols + offset)

            offset = 0

            if new_rank_code > ord("z"):
                offset += 1
                new_rank_code -= ALPHABET_SIZE

            rank += chr(new_rank_code)

    return rank[::-1]


def _make_ranks_length_equal(prev_rank: str, next_rank: str) -> Tuple[str, str]:
    while len(prev_rank) != len(next_rank):
        if len(prev_rank) > len(next_rank):
            next_rank += "a"
        else:
            prev_rank += "a"

    return prev_rank, next_rank


def _get_rank_codes(rank: str) -> List[int]:
    codes = []

    for char in rank:
        codes.append(ord(char))

    return codes
