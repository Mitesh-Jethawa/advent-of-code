from pathlib import Path
from math import prod
def part_1(data: list[str]):
    symbols = data[-1].split()
    numbers = list(zip(*[i.split() for i in data[:-1]]))
    numbers = [[int(i) for i in j] for j in numbers]
    return numbers, symbols

def part_2(data: list[str]):
    symbols = data[-1].split()
    array = [list(i) for i in data[:-1]]
    numbers_list = ["".join(j).strip() for j in zip(*array)]
    numbers: list[list[int]] = [[]]
    for number in numbers_list:
        if number != "":
            numbers[-1].append(int(number))
        else:
            numbers.append([])
    return numbers, symbols

def summation(numbers, symbols):
    current_sum = 0
    for col, symbol in (zip(numbers, symbols)):
        if symbol == "+":
            current_sum += sum(col)
        elif symbol == "*":
            current_sum += prod(col)
    return current_sum

data = Path(Path(__file__).parent/"day_06.txt").read_text().splitlines()
print(summation(*part_1(data)), summation(*part_2(data)))
