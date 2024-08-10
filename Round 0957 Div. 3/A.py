def solver(arr):
    arr.sort()
    for _ in range(5):
        arr[0] += 1
        arr.sort()
    print(arr[0]*arr[1]*arr[2])
    
def takeInputAndPutItInSolver():
    # int(input())
    arr = list(map(int, input().strip().split()))
    solver(arr)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()