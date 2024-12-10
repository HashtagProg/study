def solution(num_list):
    num2 = num_list[-1]
    num1 = num_list[-2]
    
    if num2 > num1:
        num_list.append(num2 - num1)
    else:
        num_list.append(num2 * 2)

    return num_list