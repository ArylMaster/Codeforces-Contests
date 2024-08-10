def solver(n, p):
    q = p[1:] + [p[0]]
    print(' '.join(list(map(str, q))))

def takeInputAndPutItInSolver():
    
    n = int(input())
    p = list(map(int, input().strip().split()))
    
    solver(n, p)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()