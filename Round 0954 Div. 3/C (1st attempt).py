def finder(n, m, s, ind, c):
    ind.sort()
    clist = list(c)
    c.sort()
    l = 0
    r = m-1
    Map = {}
    for i in ind:
        if i in Map:
            Map[i] += 1
        else:
            Map[i] = 1
    slist = list(s)
    for i in Map:
        if Map[i] == 1:
            slist[i] = clist[l]
            l += 1
        else:
            while Map[i] > 1:
                Map[i] -= 1
                r -= 1
            slist[i] = clist[l]
            l += 1
    return ''.join(slist)

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split()))
    s = input()
    ind = list(map(int, input().strip().split()))
    c = input()
    print(finder(n, m, s, ind, c))