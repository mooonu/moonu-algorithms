import math

def solution(n):
    # 루트(제곱근) 필요
    # root = math.sqrt(n)
    # if root == int(root):
    #     return (root+1) ** 2
    # else:
    #     return -1
    
    # math 없이
    root = n ** (1/2)
    if root == int(root):
        return (root+1) ** 2
    else:
        return -1