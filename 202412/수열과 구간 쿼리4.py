def solution(arr, queries):
    answer = []
    
    for i,j,z in queries:
        for idx in range(i, j + 1):
            if i <= idx <= j and idx % z == 0:
                arr[idx] += 1
    answer = arr
    
    return answer