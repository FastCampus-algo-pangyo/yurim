from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

shark_x, shark_y, shark_size = 0, 0, 2
for x in range(n):
    for y in range(n):
        if arr[x][y] == 9:
          arr[x][y] = 0
          shark_x, shark_y = x, y
          break

def bfs(shark_x, shark_y, shark_size): // bfs는 항상 최적의 경로를 탐색한다.
  fish_q = deque()
  shark_q = deque([(shark_x, shark_y)])
  distance = [[0] * n for _ in range(n)]  
  while shark_q:
    cx, cy = shark_q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = cx+dx, cy+dy
      if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] <= shark_size and distance[nx][ny] == 0:
          shark_q.append((nx, ny))
          distance[nx][ny] = distance[cx][cy] + 1
          if arr[nx][ny] < shark_size and arr[nx][ny]!= 0:
            fish_q.append((nx, ny, distance[nx][ny]))          
  return sorted(fish_q, key=lambda x: (x[2], x[0], x[1]))

shark_eat = 0
total_time = 0
while True:
  fish_list = bfs(shark_x, shark_y, shark_size)  
  if len(fish_list) != 0:
    shark_x, shark_y, time = fish_list[0]  
    arr[shark_x][shark_y] = 0
    total_time += time    
    shark_eat += 1
    if shark_eat == shark_size:
      shark_eat = 0
      shark_size += 1      
  else:
    break
print(total_time)
