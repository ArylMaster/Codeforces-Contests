def HCF(a, b):
    maxi = max(a, b)
    mini = min(a, b)
    if mini == 0:
        return maxi
    return HCF(mini, maxi%mini)


def beautyOfTheMountains():
    n, m, k = list(map(int, input().strip().split()))
    matrix, binary = [], []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    for _ in range(n):
        binary.append(list(input()))

    withSC = withoutSC = 0
    for i in range(n):
        for j in range(m):
            if binary[i][j] == '1':
                withoutSC += matrix[i][j]
            else:
                withSC += matrix[i][j]
    diff = abs(withSC - withoutSC)
    if diff == 0:
        return "YES"
    factors = []
    for q in range(n-k+1):
        for w in range(m-k+1):
            total = 0
            for i in range(q, q+k):
                for j in range(w, w+k):
                    if binary[i][j] == '1':
                        total += 1
                    else:
                        total -= 1
            factors.append(abs(total))
    for f in factors:
        if f != 0:
            if diff % f == 0:
                return "YES"
    return "NO"

for _ in range(int(input())):
    print(beautyOfTheMountains())