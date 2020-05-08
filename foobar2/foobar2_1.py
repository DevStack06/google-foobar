def solution(h, q):
    # Your code here
    val = int(pow(2, h))-1
    p = val
    out = []
    # print(val)
    for i in q:
        temp = val
        if(val == i):
            out.append(-1)
            # print(-1)
        else:
            k = h-1
            while(1):
                # print(temp)
                p = temp
                if i <= (temp-int(pow(2, k))):
                    temp = temp-int(pow(2, k))
                    k = k-1
                else:
                    temp = temp-1
                    k = k-1
                if(temp == i):
                    out.append(p)
                    break
    return(out)


out = solution(3, [7, 3, 5, 1])
print(out)
