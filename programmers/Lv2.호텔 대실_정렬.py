from collections import deque

def solution(book_time):
    answer = 0
    queue = deque()
    book_time.sort()

    for i in range(len(book_time)):
        start, end = book_time[i]
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])

        if i == 0:
            queue.append(end + 10)
            answer += 1
        else:
            flag = False
            for time in queue:
                if start >= time:
                    queue.remove(time)
                    queue.append(end+10)
                    flag = True
                    break
            if not flag:
                queue.append(end+10)
                answer += 1

    return answer
