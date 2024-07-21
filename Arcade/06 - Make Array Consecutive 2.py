def solution(statues):
    x = [0] * 21
    count = 0
    for i in statues:
        x[i] += 1
    start = min(statues)
    end = max(statues)
    for i in range(start, end + 1):
        if x[i] == 0:
            count += 1
    print("solution(statues) =", count)
    return count

statues = [6, 2, 3, 8]    
solution(statues)
