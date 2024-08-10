def solver(n, s, m, arr):
    if arr[0][0] >= s:
        print("YES")
        return
    for i in range(1, n):
        if arr[i][0] - arr[i-1][1] >= s:
            print("YES")
            return
        
    if m - arr[n-1][1] >= s:
        print( "YES")
        return
    
    print("NO")
    

    
    
    pass

def takeInputAndPutItInSolver():
    # int(input())
    n, s, m = list(map(int, input().strip().split()))
    arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
    solver(n, s, m, arr)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()