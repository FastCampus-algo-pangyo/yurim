N = int(input())
memory = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
    count = 0 
    for j in range(N):
        if answer[j] == 0: 
            if count == memory[i]:
                answer[j] = i + 1
                break
            count += 1

print(*answer)