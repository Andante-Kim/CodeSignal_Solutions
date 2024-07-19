def solution(year):
    print("solution(year) = {}".format(year))
    if year%100 == 0:
        century = year//100
    else:
        century = (year + 100)//100
    return century
    
solution(1905)
