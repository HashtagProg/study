def solution(ineq, eq, n, m):
    answer = 0

    if (ineq, eq) == ('<', '='):
        answer = int(n <= m)
    elif (ineq, eq) == ('>', '='):
        answer = int(n >= m)
    elif (ineq, eq) == ('<', '!'):
        answer = int(n < m)
    elif (ineq, eq) == ('>', '!'):
        answer = int(n > m)
    else:
        return 'wrong input'
    print(answer)
    return answer

solution('>','=',3,2)