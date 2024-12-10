def solution(numLog):
    answer = ''
    stand = { 1:'w', -1:'s', 10:'d', -10:'a'}
    
    for num in range(1, len(numLog)):
        key = numLog[num] - numLog[num - 1]
        answer += stand[key]

    return answer