from pathlib import Path
data = Path(Path(__file__).parent/"day_05.txt").read_text().splitlines()
seperator = data.index("")
id_ranges: list[tuple[int, int]] = [(int(a), int(b)) for a, b in (x.split("-") for x in data[:seperator])]
available_ids = [int(i) for i in data[seperator + 1:]]
password1 = 0
sorted_ranges = sorted(id_ranges)
merged_ranges = []
current_start, current_end = sorted_ranges[0]
for start, end in sorted_ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end
merged_ranges.append((current_start, current_end))
password1 = 0
for i in available_ids:
    for start, end in merged_ranges:
        if start <= i <= end:
            password1 += 1
            break
password2 = sum(end - start + 1 for start, end in merged_ranges)
print(password1, password2)
