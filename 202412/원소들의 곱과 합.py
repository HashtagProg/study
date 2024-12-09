def solution(num_list):
    answer = 0
    nSum = 0
    nMul = 1
    
    for i in num_list:
        nSum += i
        nMul *= i
    
    answer = 1 if nMul < nSum**2 else 0

    return answer