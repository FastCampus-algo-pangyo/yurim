from collections import deque

def bfs():
    queue = deque([1])
    visited[1] = 1
    count = 0
    
    while queue:
        current = queue.popleft()
        
        for neighbor in adj_list[current]:
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = 1
                count += 1
                
    return count

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)  

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)  

print(bfs())
