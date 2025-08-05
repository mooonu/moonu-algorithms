def solution(arr, divisor):
    answer = []
    
    for i in sorted(arr):
        if i % divisor is 0:
            answer.append(i)
    
    if not answer:
        answer = [-1]
    
    return answer