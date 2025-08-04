def solution(absolutes, signs):
    # True, False를 어떻게 부호로 ?
    # is idx[0] is False 이면 빼고
    
    L = []
    
    for i in range(len(signs)):
        if signs[i] is False:
            L.append(-absolutes[i])
        else:
            L.append(absolutes[i])
    return sum(L)