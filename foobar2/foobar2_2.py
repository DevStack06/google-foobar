def solution(l):
    # Your code here
    dicti = {}
    for i in l:
        val = i.split('.')
        k = [100000, 1000, 1]
        d = 0
        key = 0
        # print(val)
        for j in val:
            key = key+(int(j)+1)*k[d]
            d = d+1
        # print(key)
        dicti[key] = i
    out = []
    for i in sorted(dicti.keys()):
        out.append(dicti[i])
    return out


out = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
print(out)
