from functools import cache
from pathlib import Path
import re
import time
start = time.perf_counter()

data = Path(Path(__file__).parent/"day_11.txt").read_text().splitlines()
routes:dict[str, list[str]] = {}
for i in data:
    source, *destinations = re.findall(r"\w{3}", i)
    routes[source] = destinations

@cache
def count_paths(source:str):
    if source == "out":
        return 1
    return sum(count_paths(i) for i in routes[source])

@cache
def count_paths_2(source:str, passed: int):
    if source == "out":
        return (passed == 2)
    elif source == "dac" or source == "fft":
        passed += 1
    return sum(count_paths_2(i, passed) for i in routes[source])

print(count_paths("you"), count_paths_2("svr", 0), time.perf_counter()-start)