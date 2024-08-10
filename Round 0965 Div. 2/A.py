def solver(xc, yc, k):
    x = []
    y = []
    if k % 2 == 1:
        x.append(xc)
        y.append(yc)
    
    for i in range(1, k//2 + 1):
        x.append(xc + i)
        y.append(yc + i)
        x.append(xc - i)
        y.append(yc - i)
    
    for i in range(k):
        print(f"{x[i]} {y[i]}")

def takeInputAndPutItInSolver():
    '''
    int(input())
    list(map(int, input().strip().split()))
    '''
    xc, yc, k = list(map(int, input().strip().split()))


    solver(xc, yc, k)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()