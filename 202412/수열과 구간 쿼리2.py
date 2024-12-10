def solution(arr, queries):
    answer = []
    
    for i,j,z in queries:
        temp = []
        for num in range(i,j+1):
            if arr[num] > z:
                temp.append(arr[num])
        
        answer.append(min(temp) if temp else -1)
        
    return answer