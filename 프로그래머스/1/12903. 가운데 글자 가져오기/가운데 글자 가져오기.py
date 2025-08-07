def solution(s):
    # 가운데를 어떻게 판별하지
    # 길이 // 2 -> 인덱스값 나오고 그거에 -1 한거랑 같이 하면 짝수 중간 나옴
    # 홀수도 길이 // 2 -> 인덱스값나오고 그거 그대로 하면 중간 나옴
    
    idx = len(s) // 2
    if len(s) % 2 == 0: #짝수
        return s[idx-1]+s[idx]
    else:
        return s[idx]