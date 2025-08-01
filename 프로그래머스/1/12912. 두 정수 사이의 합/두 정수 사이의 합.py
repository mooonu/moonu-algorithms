def solution(a, b):
    L = []
    if a == b:
        return a
    elif a < b:
        for i in range(int(a), int(b+1)):
            L.append(i)
        return sum(L)
    else:
        for i in range(b, (a+1)):
            L.append(i)
        return sum(L)
            