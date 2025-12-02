with open("day_01.txt") as f:
    lines = f.read().splitlines()
current, password1, password2 = 50, 0, 0
for line in lines:
    direction, number = line[0], line[1:]
    number = int(number)
    if direction == "L":
        number *= -1
    if current*(number + current) < 0 or (number + current) == 0:
        password2 += 1
    if current == 0:
        password1 += 1
    password2 += abs(number + current)//100
    current = (current + number) % 100   

print(password1, password2)