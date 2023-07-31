N, K = map(int, input().split())
circle_q = [ i for i in range(1, N+1)]
result = []

index = 0
while circle_q:
  index = (index + (K-1)) % len(circle_q)
  result.append(circle_q.pop(index))

print("<" + ", ".join(map(str, result)) + ">") 
