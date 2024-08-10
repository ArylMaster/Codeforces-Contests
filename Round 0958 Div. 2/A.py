def solver(n, k):
    ops = 0
    while n > k:
        n = n-k+1
        ops += 1
    if n == 1:
        print(ops)
    else:
        print(ops+1)
    pass

def takeInputAndPutItInSolver():
    # int(input())
    n, k = list(map(int, input().strip().split()))
    solver(n, k)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()