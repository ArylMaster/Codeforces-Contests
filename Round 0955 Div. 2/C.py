def finder(n, l, r, a):
    wins = 0
    left = right = 0
    tempSum = a[0]
    while True:
        if l <= tempSum <= r:
            wins += 1
            right += 1
            left = right
            if right < n:
                tempSum = a[right]
            else:
                break
        elif tempSum < l:
            right += 1
            if right < n:
                tempSum += a[right]
            else:
                break
        else:
            tempSum -= a[left]
            left += 1
            if tempSum == 0:
                right += 1
                if right < n:
                    tempSum = a[right]
                else:
                    break
    return wins

for _ in range(int(input())):
    n, l, r = list(map(int, input().strip().split()))
    print(finder(n, l, r, list(map(int, input().strip().split()))))