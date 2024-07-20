def solution(n):
    count = 0
    line = 1
    for i in range(n):
        if i == 0:
            count += line
        else:
            line += 2
            count += line
    for k in range(n-1):
        line -= 2
        count += line
    print("solution(n) = {}".format(count))
    return count

solution(4)            
