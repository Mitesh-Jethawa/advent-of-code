from ast import literal_eval
from pathlib import Path
from itertools import combinations
import time
SYMBOL_MAP = {".":"0", "#":"1"}
start = time.perf_counter()
def bits_to_int(t:tuple[int, ...] | int):
    if isinstance(t, int):
        return 1 << t
    return sum(1 << i for i in t)
def start_machine(machine :list[str]) -> int:
    pattern = [SYMBOL_MAP[char] for char in machine[0] if char in SYMBOL_MAP]
    pattern.reverse()
    pattern_int = int("".join(pattern), 2)
    buttons_tuples:list[tuple[int, ...] | int] = [literal_eval(i) for i in machine[1:-1]]
    buttons = [bits_to_int(i) for i in buttons_tuples]
    moves = 1
    while True:
        for combination in combinations(buttons, moves):
            current_pattern = pattern_int
            for button in combination:
                current_pattern = current_pattern^button
            if current_pattern == 0:
                return moves
        moves += 1

data = [line.split() for line in Path(Path(__file__).parent/"day_10.txt").read_text().splitlines()]
password_1 = sum(map(start_machine, data))
print(password_1, time.perf_counter() - start)