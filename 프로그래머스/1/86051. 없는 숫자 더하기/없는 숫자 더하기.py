def solution(numbers):
    # 배열안에 없는 값을 찾아서 더하고 리턴
    
    # 아래 정의한 리스트는 정말정말 비효율적
    # L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # 차라리 이렇게 쓰자
    
    L = list(range(0, 10))
    diff = list(set(L) - set(numbers))
    return sum(diff)
