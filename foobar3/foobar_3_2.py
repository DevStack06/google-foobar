def solution(l):
    # Your code here
    n = len(l)
    count = 0
    mat = []
    for i in range(0, n):
        mat.append(0)
    for j in range(0, n-1):
        i = 0
        while(i < j):
            if l[j] % l[i] == 0:
                mat[j] = mat[j]+1
            i = i+1

    for k in range(2, n):
        j = 0
        while(j < k):
            if l[k] % l[j] == 0:
                count = count+mat[j]
            j = j+1

    return count


print(solution([1, 2, 3, 4, 5, 6]))
