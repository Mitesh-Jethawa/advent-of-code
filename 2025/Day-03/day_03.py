from pathlib import Path
def highest_joltage(number: str, k: int):
    start = 0
    result = ""
    for p in range(k):
        end = len(number) - (k - p - 1)
        highest_digit = max(number[start:end])
        result += highest_digit
        start = number.find(highest_digit, start, end) + 1
    return int(result)
numbers = Path(Path(__file__).parent/"day_03.txt").read_text().splitlines()
password1 = sum([highest_joltage(str(number), 2) for number in numbers])
password2 = sum([highest_joltage(str(number), 12) for number in numbers])
print(password1, password2)