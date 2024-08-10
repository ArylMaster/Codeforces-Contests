def permutation_giver(p, n):
    q = {}
    indices = {}
    numsUsed = {k:1 for k in range(1, n+1)}
    for i in range(n):
        indices[p[i]] = i

    if indices[1] == 0 or indices[1] == n-1:
        isEven = True
    else:
        if indices[1] % 2 == 0:
            isEven = True
        else:
            isEven = False

    if isEven:
        for i in range(1, n-1, 2):
            num = n + 2 - p[i]
            q[i] = num
            numsUsed[num] = 0
        numsLeft = []
        for i in range(n, 0, -1):
            if numsUsed[i] == 1:
                numsLeft.append(i)
        for i in range(n, 0, -1):
            index = indices[i]
            if index not in q:
                q[index] = numsLeft.pop()
    
    else:
        for i in range(2, n, 2):
            num = n + 2 - p[i]
            q[i] = num
            numsUsed[num] = 0
        numsLeft = []
        for i in range(n, 0, -1):
            if numsUsed[i] == 1:
                numsLeft.append(i)
        for i in range(n, 0, -1):
            index = indices[i]
            if index not in q:
                q[index] = numsLeft.pop()

    string = ''
    for i in range(n):
        string += str(q[i]) + " "

    return string.rstrip()



output = []
t = int(input())

for i in range(t):
    n = int(input())
    output.append(permutation_giver(list(map(int, input().split())), n))

for i in output:
    print(i)

    
