from pathlib import Path
grid = [list(i) for i in Path(Path(__file__).parent/"day_04.txt").read_text().splitlines()]
def find_password(grid: list[list[str]]) -> tuple[list[list[str]], int]:
    rows, cols = len(grid), len(grid[0])
    directions = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x or y)]
    password = 0
    new_grid = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            count = 0
            if grid[r][c] != "@":
                continue
            for x, y in directions:
                new_x, new_y = r+x, c+y
                if not (0 <= new_x < rows and 0 <= new_y < cols):
                    continue
                if grid[new_x][new_y] == "@":
                    count += 1
            if count < 4:
                new_grid[r][c] = "."
                password += 1
    return new_grid, password

password1 = find_password(grid)[1]
password2 = 0
boxes_removed = -1
while boxes_removed != 0:
    new_grid, boxes_removed = find_password(grid)
    grid = new_grid
    password2 += boxes_removed
print(password1, password2)
