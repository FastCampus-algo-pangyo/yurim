from collections import deque

def bfs():
    time = 0
              
    while dochi_q:
        
        for _ in range(len(water_q)): // 물 분사
            cx, cy = water_q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < r and 0 <= ny < c and map[nx][ny] == '.' and visited[nx][ny] == 0:
                    water_q.append((nx, ny))
                    visited[nx][ny] = 1

        for _ in range(len(dochi_q)): // 고슴도치 이동
            cx, cy = dochi_q.popleft()
            if map[cx][cy] == 'D':
                return time
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < r and 0 <= ny < c and (map[nx][ny] == '.' or map[nx][ny] == 'D') and visited[nx][ny] == 0:
                    dochi_q.append((nx, ny))
                    visited[nx][ny] = 1
        time += 1
      
    return 'KAKTUS'

r, c = map(int, input().split())
map = [list(input()) for _ in range(r)]

water_q = deque()
dochi_q = deque()
visited = [[0] * c for _ in range(r)]

for i in range(r):
  for j in range(c):
    if map[i][j] == '*':
      water_q.append((i, j))
      visited[i][j] = 1
    elif map[i][j] == 'S':
      dochi_q.append((i, j))
      visited[i][j] = 1
      
print(bfs())
