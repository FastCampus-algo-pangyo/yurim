from itertools import combinations
import copy  

def solution(archer_positions):
  count = 0
  attack_list = [] 
  
  for archer_position in archer_positions:
    archer_x, archer_y = archer_position[0], archer_position[1]
    attack = []
    
    for x in range(archer_x): 
      for y in range(m):
        if map_copy[x][y] == 1: 
          distance = abs(x - archer_x) + abs(y - archer_y)
          if (distance <= d): 
            attack.append((x, y, distance)) 

    if attack:
      attack_list.append(sorted(attack, key=lambda x: (x[2],x[1]))[0]) 

  for x, y, distance in attack_list:
    if map_copy[x][y] == 1: 
      map_copy[x][y] = 0 
      count += 1 

  return count

n, m, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
archer_y = [i for i in range(m)]

result = 0

for archer_y in combinations(archer_y, 3):
    count = 0
    map_copy = copy.deepcopy(map)  
  
    for archer_x in range(n, 0, -1):
      archer_positions = [(archer_x, archer_y[0]), (archer_x, archer_y[1]), (archer_x, archer_y[2])]
      count += solution(archer_positions)
    
    result = max(result, count)

print(result)