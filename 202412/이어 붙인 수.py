def solution(num_list):
    answer = 0
    
    holsu = ''
    jaksu = ''
    
    for num in num_list:
        if num % 2 == 0:
            jaksu += str(num)
        elif num % 2 == 1:
            holsu += str(num)

    answer = int(jaksu) + int(holsu)
    
    return answer