n = int(input())
score = [0] + [int(input()) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
  dp[i][0] = max(dp[i-1][1], dp[i-1][2])
  dp[i][1] = dp[i-1][0] + score[i]
  dp[i][2] = dp[i-1][1] + score[i]

result = max(dp[n][1], dp[n][2])
print(result)