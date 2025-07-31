def solution(n):
    # x는 2보다 커야하고 n 보다 작아야함
    # x를 하나씩 증가하며 나머지가 1이 되는 첫번째 수가 가장 작은 자연수
    for x in range(2, n):
        if n % x == 1:
            return x