def solver(n, m, k):
    for i in range(n, m, -1):
        print(i, end=' ')
    for i in range(1, m+1):
        print(i, end=' ')
    print()

def takeInputAndPutItInSolver():
    # int(input())
    n, m, k = list(map(int, input().strip().split()))
    solver(n, m, k)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()