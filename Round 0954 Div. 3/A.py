def finder(x1, x2, x3):
    dist = float("inf")
    for i in range(1, 11):
        dist = min(abs(x1 - i) + abs(x2 - i) + abs(x3 - i), dist)
    return dist

for _ in range(int(input())):
    x1, x2, x3 = list(map(int, input().strip().split()))
    print(finder(x1, x2, x3))