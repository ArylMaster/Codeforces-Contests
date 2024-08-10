def collatzConjecture(x, y, k):
    looperMap = [x]
    xMap = {x:0}
    i = 1
    while k > 0:
        rem = x%y
        ops = y - rem
        if ops <= k:
            k -= ops
            x += ops
        else:
            x += k
            k = 0
        while x % y == 0:
            x //= y
        if x in xMap:
            modder = len(looperMap) - xMap[x]
            k %= modder
        else:
            looperMap.append(x)
            xMap[x] = i
            i += 1
    return x

for _ in range(int(input())):
    x, y, k = list(map(int, input().strip().split()))
    print(collatzConjecture(x, y, k))