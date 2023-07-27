from collections import deque

n = int(input())
friends = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    friend = input()
    for j in range(n):
        if friend[j] == 'Y':
            friends[i][j] = 1

def bfs(start):
    visited = [0] * n
    visited[start] = 1
    queue = deque([(start, 0)])  
    count = 0
    while queue:
        current, distance = queue.popleft()
        if distance >= 2:
            continue
            
        for next in range(n):
            if not visited[next] and friends[current][next]:
                count += 1
                visited[next] = 1
                queue.append((next, distance + 1))  
                
    return count

answer = 0
for start in range(n):
    answer = max(answer, bfs(start))
print(answer)
