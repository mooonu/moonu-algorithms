def solution(a, b):
    # result = 0
    # for i in range(len(a)):
    #     result += a[i] * b[i]
    # return result
    return sum(x * y for x, y in zip(a, b))