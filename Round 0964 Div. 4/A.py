def solver(n):
    print( n//10 + n%10)

def takeInputAndPutItInSolver():
    # int(input())
    # list(map(int, input().strip().split()))
    solver(int(input()))

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()