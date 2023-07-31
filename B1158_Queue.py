N, K = map(int, input().split())
circle = [ i for i in range(1, N+1)]
result = []

index = 0
while circle:
  index = (index + (K-1)) % len(circle)
  result.append(circle.pop(index))

print("<" + ", ".join(map(str, result)) + ">") 