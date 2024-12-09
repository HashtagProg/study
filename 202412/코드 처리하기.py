def solution(code):
    ret = ''
    mode = 0

    for idx, i in enumerate(code):
        if i == '1':
            mode = 0 if mode == 1 else 1
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret += i
            elif mode == 1:
                if idx % 2 == 1:
                    ret += i
        idx += 1
    print('result : ' + ret)

    return ret if ret else 'EMPTY'

    # acbac
solution('abc1abc1abc')