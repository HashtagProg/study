def solution(a, d, included):
    answer = 0
    num = 0 
    for idx, flag in enumerate(included):
        if idx == 0:
            num = a
        else:
            num += d
        
        if flag:
            answer += num
    
    return answer