def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_idx = arr.index(min(arr))
        arr.pop(min_idx)
        return arr