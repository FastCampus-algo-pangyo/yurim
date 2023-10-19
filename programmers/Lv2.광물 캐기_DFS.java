from collections import Counter

costs = [[1,1,1],[5,1,1],[25,5,1]]
index = {'diamond' : 0,'iron': 1,'stone': 2}

answer = []

def dfs(picks, minerals, total_cost):
    if sum(picks) == 0 or not minerals:
        return answer.append(total_cost)
        
    mineral_counts = Counter(minerals[:5])

    available_index = []
    for i, pick in enumerate(picks):
        if pick != 0:
            available_index.append(i)

    for i in available_index:
        cost = 0
        for key, value in mineral_counts.items():
            cost += value * costs[i][index[key]]
        picks[i] -= 1
        dfs(picks, minerals[5:], cost + total_cost)
        picks[i] += 1

def solution(picks, minerals):
    dfs(picks, minerals, 0)
    return min(answer)
