def finder(n, k, a):
    a.sort()
    ops = 0
    if n % 2 == 0:
        for i in range(n-1):
            done = False
            if a[i] is not None:
                for j in range(i+1, n):
                    if a[j] is not None:
                        if (max(a[i], a[j]) - min(a[i], a[j]))%k == 0:
                            ops += (max(a[i], a[j]) - min(a[i], a[j]))//k
                            a[i] = a[j] = None
                            done = True
                if not done:
                    return -1
        return ops
    else:
        pass
