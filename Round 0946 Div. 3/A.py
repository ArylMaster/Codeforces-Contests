def finder(ls):
    x, y = ls[0], ls[1]
    if y % 2 == 0:
        screens = y//2
        x = x - (screens*7)
        if x <= 0:
            return screens
        screens += x//15
        x = x%15
        if x > 0:
            screens += 1
        return screens
    else:
        screens = y//2 + 1
        x = x - (screens-1)*7
        x -= 11
        if x <= 0:
            return screens
        screens += x//15
        x = x%15
        if x > 0:
            screens += 1
        return screens



t = int(input())
output = []
for i in range(t):
    output.append(finder(list(map(int, input().split()))))

for i in output:
    print(i)