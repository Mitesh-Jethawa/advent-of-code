from pathlib import Path
from functools import cache

@cache
def count_timelines(grid: tuple[tuple[int]], x:int, y:int) -> int:
    if y == len(grid) - 1:
        return 1
    elif grid[y][x] == 1:
        return count_timelines(grid, x-1, y+1) + count_timelines(grid, x+1, y+1)
    elif grid[y][x] == 0 or grid[y][x] == 2:
        return count_timelines(grid, x, y+1)
    else:
        return 0
    
SYMBOL_VALUES = {".":0, "^":1, "S":2}
grid = tuple(tuple(SYMBOL_VALUES[i] for i in j) for j in Path(Path(__file__).parent/"day_07.txt").read_text().splitlines())
initial_laser = grid[0].index(2)
lasers_dict = dict.fromkeys(range(len(grid[0])), 0)
lasers_dict[initial_laser] = 1
laser_hits: set[int] = set()
hits = 0
for row in grid:
    for laser in lasers_dict:
        if row[laser] == 1 and lasers_dict[laser]:
            laser_hits.add(laser)
    for laser in laser_hits:
            numbers = lasers_dict[laser]
            lasers_dict[laser-1] += numbers
            lasers_dict[laser+1] += numbers
            lasers_dict[laser] = 0
    hits += len(laser_hits)
    laser_hits = set()
timelines = sum(lasers_dict.values())
print(hits, timelines)
print(count_timelines(grid, initial_laser, 0))