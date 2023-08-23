def calc_distance(selected_chickens):
    city_chicken_distance = 0
    for house in houses:
        chicken_distance = float('inf')
        for chicken in selected_chickens:
            distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            chicken_distance = min(chicken_distance, distance)
        city_chicken_distance += chicken_distance
    global min_distance
    min_distance = min(min_distance, city_chicken_distance)

def combinations(depth, index):
    if depth == m:
        selected_chickens = [chickens[i] for i in range(len(chickens)) if selected[i]]
        calc_distance(selected_chickens)
        return

    for i in range(index, len(chickens)):
        selected[i] = True
        combinations(depth + 1, i + 1)
        selected[i] = False

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            houses.append((i, j))
        elif grid[i][j] == 2:
            chickens.append((i, j))

selected = [False] * len(chickens)
min_distance = float('inf')
combinations(0, 0)
print(min_distance)
