def solution(n, control):
    stand = { 'w':1, 's':-1, 'd':10, 'a':-10 }
    
    for word in control:
        n += stand[word]

    return n