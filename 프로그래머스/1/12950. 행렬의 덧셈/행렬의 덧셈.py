def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        L = []
        for j in range(len(arr1[i])):
            L.append(arr1[i][j] + arr2[i][j])
        result.append(L)
        
        
    return result