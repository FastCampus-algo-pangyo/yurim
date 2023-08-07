my_string = input()
stack = []
laser_positions = set()
bar_positions = []

for i, char in enumerate(my_string):
    if char == "(":
        stack.append(i)
    elif char == ")" and stack:
        start = stack.pop()
        if i - start == 1:
            laser_positions.add(start)
        else:
            bar_positions.append((start, i))

total_count = 0

for start, end in bar_positions:
    count = 1
    for pos in laser_positions:
        if start < pos < end:
            count += 1
    total_count += count

print(total_count)