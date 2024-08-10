def solver(n):
    if n == 1:
        print(1)
        print(1)
        return 
    a = list(bin(n)[2:])
    arr = [n]
    l = len(a)-1
    converted = False
    while l >= 0:
        if a[l] == '1':
            a[l] = '0'
            arr.append(int(''.join(a), 2))
            converted = True
        else:
            if converted:
                a[l] = '1'
                converted = False
            l -= 1
    print(len(arr))
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=' ')
    print()
    pass

def solverNew(n):
    arr = [n]
    while True:
        ans = float("inf")
        last = arr[-1]
        l = 1
        r = last-1
        while l <= r:
            mid = (l+r)//2
            if mid|last == n:
                pass

    pass

def takeInputAndPutItInSolver():
    n = int(input())
    # list(map(int, input().strip().split()))
    solver(n)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()