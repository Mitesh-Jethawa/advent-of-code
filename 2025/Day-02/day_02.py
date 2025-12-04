from pathlib import Path
number_list = Path(Path(__file__).parent/"day_02.txt").read_text().split(",")
number_range_int: list[tuple[int, int]] = [(int(a), int(b)) for a, b in (x.split("-") for x in number_list)]
password1, password2 = 0, 0
invalid_ids = [int(str(number)*2) for number in range(1,100000)]
complete_invalid_ids = list(set([int(str(number)*i) for i in range (2,12) for number in range(1,10**(11//i))]))
for number_range in number_range_int:
    start,end = number_range
    for invalid_id in complete_invalid_ids:
        if start <= invalid_id <= end:
            password2 += invalid_id
            if (invalid_id in invalid_ids):
                password1 += invalid_id 
print(password1, password2)
# I'm intentionally not using regex , I wanted to try to do it without it, anyways it's very simple with regex
