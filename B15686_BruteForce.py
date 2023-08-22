from itertools import combinations

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

min_distance = float('inf')

for selected_chickens in combinations(chickens, m):
    city_chicken_distance = 0
    for house in houses:
        chicken_distance = float('inf')
        for chicken in selected_chickens:
            distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            chicken_distance = min(chicken_distance, distance)
        city_chicken_distance += chicken_distance
    min_distance = min(min_distance, city_chicken_distance)

print(min_distance)
