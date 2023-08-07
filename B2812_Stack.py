N, K = map(int, input().split())
number = list(input().strip())

stack = [number[0]]

for num in number[1:]:
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

stack = stack[:-K] if K > 0 else stack

result = ''.join(stack)
print(result)
