def solver(n, alt):
    arr = []
    preComp = [float("-inf")]*n
    for i in range(1, n):
        pass
    for i in range(1, n):
        if i == 1 or i == n-1:
            arr.append('1')
            continue



def takeInputAndPutItInSolver():
    n, m = list(map(int, input().strip().split()))
    alt = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = list(map(int, input().strip().split()))
        alt[u].append(v)

    solver(n, alt)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()