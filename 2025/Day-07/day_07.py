from pathlib import Path
SYMBOL_VALUES = {".":0, "^":1, "S":2}
grid = [[SYMBOL_VALUES[i] for i in j] for j in Path(Path(__file__).parent/"day_07.txt").read_text().splitlines()]
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
