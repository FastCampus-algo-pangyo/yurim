def dfs(row, count, queen_positions):
    if row == n:
        return count + 1

    for col in range(n):
        attacked = False
        for prev_row, prev_col in queen_positions:
            if col == prev_col or abs(row - prev_row) == abs(col - prev_col):
                attacked = True
                break
        if attacked:
            continue

        queen_positions.append((row, col))
        count = dfs(row + 1, count, queen_positions)
        queen_positions.pop()

    return count

n = int(input())
answer = 0
queen_positions = []
answer = dfs(0, 0, queen_positions)
print(answer)