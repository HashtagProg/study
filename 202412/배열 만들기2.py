def solution(l, r):
    answer = []
    flag = False
    for num in range(l, r + 1):
        for txt in str(num):
            if txt != '5' and txt != '0':
                flag = True
        if flag:
            flag = False
            continue
        answer.append(num)
        
    return answer if answer else [-1]