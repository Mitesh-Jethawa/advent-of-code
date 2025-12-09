from itertools import combinations
from math import dist, prod
from pathlib import Path
from scipy.cluster.hierarchy import DisjointSet
data = Path(Path(__file__).parent/"day_08.txt").read_text().splitlines()
position_dictionary = {i:tuple(map(int, line.split(','))) for i,line in enumerate(data)}
all_combinations = list(combinations(range(len(data)), 2))
all_combinations.sort(key= lambda x: dist(position_dictionary[x[0]], position_dictionary[x[1]]))
ds = DisjointSet(range(len(data)))
for a, b in all_combinations[:1000]:
    ds.merge(a, b)
all_subsets = ds.subsets()
all_subsets.sort(key=lambda x: len(x), reverse=True)
print(prod([len(subset) for subset in all_subsets[:3]]))

ds = DisjointSet(range(len(data)))
total_sets = 1000
for a, b in all_combinations:
    if ds.merge(a, b):
        total_sets -= 1
    if total_sets == 1:
        print(position_dictionary[a][0]*position_dictionary[b][0])
        break