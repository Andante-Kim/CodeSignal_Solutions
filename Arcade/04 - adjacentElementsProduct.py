def solution(inputArray):
    max_num = -1000000
    for i in range(len(inputArray)-1):
        if inputArray[i]*inputArray[i+1] > max_num:
            max_num = inputArray[i] * inputArray[i+1]
    print("solution(inputArray) = {}".format(max_num))
    return max_num

inputArray = [3, 6, -2, -5, 7, 3]

solution(inputArray)
        
