from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    flag = False
    
    def bfs(sx, sy, sec):
        nonlocal flag
        q = deque()
        v = [[0] * m for _ in range(n)]
        
        q.append((sx, sy))
        v[sx][sy] = sec
        
        while q:
            cx, cy = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy              
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and v[nx][ny] == 0:
                    if maps[nx][ny] == 'L':
                        flag = True
                        return v[cx][cy]
                    if maps[nx][ny] == 'E' and flag:                       
                        return v[cx][cy] + 1
                    q.append((nx, ny))
                    v[nx][ny] = v[cx][cy] + 1
        return -1
        
                    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                result = bfs(i, j, 1)
                break
    if not flag:
        return -1
    else:
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 'L':
                    answer = bfs(i, j, result)
    return answer
