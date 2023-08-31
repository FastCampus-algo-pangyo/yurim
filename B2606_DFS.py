def dfs(current):
    global count
    visited[current] = 1
    count += 1
    
    for neighbor in adjacency_list[current]:
        if visited[neighbor] == 0:
            dfs(neighbor)
            
    return count-1

N = int(input())
M = int(input())
adjacency_list = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())
    adjacency_list[s].append(e)
    adjacency_list[e].append(s)  

count = 0
print(dfs(1))
