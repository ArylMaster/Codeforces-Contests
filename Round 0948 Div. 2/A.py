def finder(n, m):
    if n < m:
        return "No"
    if n == m:
        return "Yes"
    diff = n-m
    if diff%2 == 0:
        return "Yes"
    return "No"

t = int(input())
for _ in range(t):
    n, m = input().split()
    print(finder(int(n), int(m)))
