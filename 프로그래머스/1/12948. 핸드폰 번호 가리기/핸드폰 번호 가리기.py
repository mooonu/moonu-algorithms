def solution(phone_number):
    #문자열 슬라이싱
    a = phone_number[-4::]
    b = '*' * (len(phone_number) - 4)
    return b+a