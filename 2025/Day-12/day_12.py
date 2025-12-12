from pathlib import Path

def compare_area(line:str):
    rectange, *numbers = line.split()
    rectange_area = int(rectange[0:2])*int(rectange[3:5])
    present_area = 0
    for i, number in enumerate(numbers):
        present_area += shapes_area[i]*int(number)
    return rectange_area > present_area

shapes_area = {0:7, 1:6, 2:7, 3:5, 4:7, 5:7}
data = Path(Path(__file__).parent/"day_12.txt").read_text().splitlines()[30:]
total = 0
for line in data:
    total += compare_area(line)
print(total)