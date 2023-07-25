def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

N = int(input())
heights = list(map(int, input().split()))
maxViewCount = 0

for i in range(N):
    viewCount = 0
    maxSlopeRight = -float('inf') // 음의 무한대로 초기화
    for j in range(i+1, N):
        slopeRight = slope(i, heights[i], j, heights[j])
        if maxSlopeRight < slopeRight:
            maxSlopeRight = slopeRight
            viewCount += 1

    minSlopeLeft = float('inf') // 양의 무한대로 초기화
    for j in range(i-1, -1, -1):
        slopeLeft = slope(j, heights[j], i, heights[i])
        if minSlopeLeft > slopeLeft:
            minSlopeLeft = slopeLeft
            viewCount += 1

    maxViewCount = max(maxViewCount, viewCount)

print(maxViewCount)
