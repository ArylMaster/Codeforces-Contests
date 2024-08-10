def solver(n, k, a):
    a.sort()
    S = 0
    divider = (10**9 + 7)


    mid = (k+1)//2
    left = mid - 1


    factorial = [1]
    i = 1
    for j in range(mid, n-mid+1):
        factorial.append((factorial[-1]*j)//i % divider)
        i += 1


    l, r = 0, len(factorial)-1
    for p in range(mid-1, n-mid+1):
        if a[p] == 1:
            S += (factorial[l] * factorial[r])
        l += 1
        r -= 1

    print(S % divider)
    return





























def takeInputAndPutItInSolver():
    # int(input())
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    solver(n, k, a)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()