def soccer(x1, y1, x2, y2):
    if (x1 < y1 and x2 < y2) or (x1 > y1 and x2 > y2):
        return "YES"
    return "NO"

for _ in range(int(input())):
    x1, y1 = list(map(int, input().strip().split()))
    x2, y2 = list(map(int, input().strip().split()))
    print(soccer(x1, y1, x2, y2))