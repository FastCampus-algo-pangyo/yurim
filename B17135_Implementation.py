from itertools import combinations
import copy  

def solution(archer_positions):
  count = 0
  attack_list = [] 
  
  for archer_position in archer_positions:
    archer_x, archer_y = archer_position[0], archer_position[1]
    attack = []
    
    for x in range(archer_x): # 현재 궁수가 위치한 줄까지만
      for y in range(m):
        if map_copy[x][y] == 1: # 적이 있을 경우
          distance = abs(x - archer_x) + abs(y - archer_y) # 궁수와 적의 위치를 계산
          if (distance <= d): # 반경 내에 존재할 경우
            attack.append((x, y, distance)) # 공격 가능 리스트에 추가

    if attack:
      attack_list.append(sorted(attack, key=lambda x: (x[2],x[1]))[0]) # 가장 가까운 적이고, 가장 왼쪽에 있는 적을 공격

  for x, y, distance in attack_list: # 각 궁수마다 공격할 적의 위치를 파악
    if map_copy[x][y] == 1: # 모든 궁수는 동시에 공격한다. > 같은 적이 여러 궁수에게 공격당할 수 있다.
      map_copy[x][y] = 0 # 공격 받은 곳은 적을 제거시켜서 카운트 값이 여러번 증가하지 않도록 만든다.
      count += 1 

  return count

n, m, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
archer_y = [i for i in range(m)]

result = 0

for archer_y in combinations(archer_y, 3):
    count = 0
    map_copy = copy.deepcopy(map)  
  
    for archer_x in range(n, 0, -1): # 적을 밑으로 이동시키는 것이 아니라, 궁수를 위로 이동시키는 게 훨씬 효율적이다. (x 값만 변화).
      archer_positions = [(archer_x, archer_y[0]), (archer_x, archer_y[1]), (archer_x, archer_y[2])]
      count += solution(archer_positions)
    
    result = max(result, count)

print(result)