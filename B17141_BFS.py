from collections import deque
from itertools import combinations

def bfs(start, count):
    queue = deque()
    visited = [[0] * n for _ in range(n)]

    for sx, sy in start:
        queue.append((sx, sy, 0))
        visited[sx][sy] = 1

    while queue:
        cx, cy, time = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] != 1 and visited[nx][ny] == 0:
                queue.append((nx, ny, time+1))
                visited[nx][ny] = 1
                count -= 1  
    if count == 0:
        return time
              
    return float('inf')

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

virusPoint = deque()
minTime = float('inf')
count = 0

for x in range(n):
    for y in range(n):
        if lab[x][y] == 2:
            virusPoint.append((x, y))
            count += 1
        elif lab[x][y] == 0:
            count += 1

count -= m

for start in combinations(virusPoint, m):
    minTime = min(minTime, bfs(start, count))
  
print(-1 if minTime == float('inf') else minTime)

