from itertools import combinations, pairwise
from pathlib import Path
from random import shuffle
def non_intersecting(square:tuple[tuple[int, int], tuple[int, int]],
                     polygon:list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    (x1, y1), (x2, y2) = square
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    for (ax, ay), (bx, by) in polygon:
        if ax == bx and x1 < ax < x2:
            low_y  = ay if ay < by else by
            high_y = ay if ay > by else by
            if low_y < y2 and high_y > y1:
                return False
        elif ay == by and y1 < ay < y2:
            low_x  = ax if ax < bx else bx
            high_x = ax if ax > bx else bx
            if low_x < x2 and high_x > x1:
                return False
    return True

data = Path(Path(__file__).parent/"day_09.txt").read_text().splitlines()
position_list = [(int(a), int(b)) for a, b in (line.split(',') for line in data)]
adjacent_points = list(pairwise(position_list))
adjacent_points.append((position_list[-1], position_list[0]))
position_combinations = list((combinations(position_list, 2)))
# shuffle(position_combinations)
max_area_1, max_area_2 = 0, 0
for square in position_combinations:
    (x1,y1),(x2,y2) = square
    current_area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
    if current_area > max_area_1:
        max_area_1 = current_area
    if current_area > max_area_2 and non_intersecting(square, adjacent_points):
        max_area_2 = current_area

print(max_area_1, max_area_2)