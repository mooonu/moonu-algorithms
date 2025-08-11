def solution(left, right):
    # 약수의 개수가 짝수면 더하고
    # 홀수면 빼고
    
    result = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            result -= i
        else:
            result += i
            
    return result