def finder(n, p):
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (p[i]*p[j]) % ((i+1)*(j+1)) == 0:
                ans += 1
    return ans

for _ in range(int(input())):
    n = int(input())
    print(finder(n, list(map(int, input().strip().split()))))