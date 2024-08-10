def changer(mat, i, j, n, m):
    neighbors = []
    if i > 0:
        neighbors.append(mat[i-1][j])
    if i < n-1:
        neighbors.append(mat[i+1][j])
    if j > 0:
        neighbors.append(mat[i][j-1])
    if j < m-1:
        neighbors.append(mat[i][j+1])
    maxi = max(neighbors)
    if mat[i][j] > maxi:
        return maxi
    return None

def matrix(mat, n, m):
    for i in range(n):
        for j in range(m):
            a = changer(mat, i, j, n, m)
            if a is not None:
                mat[i][j] = a
            print(mat[i][j], end=" ")
        print()

for _ in range(int(input())):
    n, m = list(map(int, input().strip().split()))
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().strip().split())))
    matrix(mat, n, m)

    