def solution(inputString):
    count = 0
    for i in range(len(inputString)):
        if inputString[i] == inputString[-(i+1)]:
            continue
        else:
            count += 1
    if count == 0:
        result = True
    else:
        result = False
    print("solution(inputString) = {}".format(result))
    return result
    
solution("abac")

