def solution(a, b):
    answer = 0
    if (a + b < b + a):
        answer = int(str(b) + str(a))
    else:
        answer = int(str(a) + str(b))

    print(answer)

solution(9, 91)