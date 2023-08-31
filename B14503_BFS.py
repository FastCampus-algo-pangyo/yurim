from collections import deque

n, m = map(int, input().split())
sx, sy, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

count = 1
queue = deque([(sx, sy)])  
visited = [[0] * m for _ in range(n)]
visited[sx][sy] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global d, count

    while queue:
        cx, cy = queue.popleft()
        
        for _ in range(4):
            d = 3 if d == 0 else d - 1
            nx, ny = cx + dx[d], cy + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and room[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
                break
        else:
            nx, ny = cx - dx[d], cy - dy[d]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
                queue.append((nx, ny))
            else:
                break
    
    return count

print(bfs())
