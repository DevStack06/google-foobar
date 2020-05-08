def solution(x, y):
    # Your code here
    x = int(x)
    y = int(y)
    max1 = max(x, y)
    min1 = min(x, y)
    out = 0
    c = 0

    while min1 != 1:
        if max1 % min1 == 0:
            out = "impossible"
            break
        c = c+int(max1/min1)
        q = max1 % min1
        max1 = max(q, min1)
        min1 = min(q, min1)
    if(out == "impossible"):
        return out
    out = c+max1-1
    return out


print(solution(4, 7))
