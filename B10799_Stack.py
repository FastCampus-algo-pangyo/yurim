my_string = input()
stack = []

count = 0

for i, char in enumerate(my_string):
    if char == "(":
        stack.append(i)
    elif char == ")" and stack:
        start = stack.pop()
        if i - start == 1:
            count += len(stack) 
        else:
            count += 1

print(count)

