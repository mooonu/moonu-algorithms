def solution(left, right):
    # 약수의 개수가 짝수면 더하고
    # 홀수면 빼고
    
    
    result = 0
    for i in range(left, right+1):
        L = []
        # 순회하며 약수의 개수를 계산하는 코드
        for j in range(1, i+1):
            if i % j == 0:
                L.append(j)
        # 길이가 짝수면 더하고 아니면 빼고
        if len(L) % 2 == 0:
            result += i
        else:
            result -= i
    
    return result