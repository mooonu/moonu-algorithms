def solution(price, money, count):
    # count 만큼 price 곱해서 다 더함
    # money랑 빼고 0보다 작으면 절댓값씌워서 리턴
    # 아니면 0 리턴
    i = 1
    result = 0
    while i < count+1:
        result += price * i
        i += 1
    
    return abs(money-result) if (money-result) <0 else 0
