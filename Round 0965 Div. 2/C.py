# def solver(n, k, a, b):
#     for i in range(n):
#         a[i] = (a[i], b[i])
#     a.sort()
#     medInd = (n-1)//2
#     maxVal = float("-inf")


#     if n % 2 == 0:
#         otherMedInd = medInd + 1
#         for i in range(medInd+1, n):
#             if a[i][1] == 1:
#                 maxVal = max(maxVal, a[i][0] + a[medInd][0] + k)
#             if a[i][1] == 0 and a[medInd][1] == 0:
#                 maxVal = max(maxVal, a[i][0] + a[medInd][0])
#         for i in range(medInd+1):
#             if a[i][1] == 1:
#                 maxVal = max(maxVal, a[i][0] + a[otherMedInd][0] + k)
#             if a[i][1] == 0 and a[otherMedInd][1] == 0:
#                 maxVal = max(maxVal, a[i][0] + a[otherMedInd][0])

#     else:
#         otherMedInd = medInd - 1
#         for i in range(medInd):
#             if a[i][1] == 1:
#                 maxVal = max(maxVal, a[i][0] + a[medInd][0] + k)
#             if a[i][1] == 0 and a[medInd][1] == 0:
#                 maxVal = max(maxVal, a[i][0] + a[medInd][0])
#         for i in range(medInd, n):
#             if a[i][1] == 1:
#                 maxVal = max(maxVal, a[i][0] + a[otherMedInd][0] + k)
#             if a[i][1] == 0 and a[otherMedInd][1] == 0:
#                 maxVal = max(maxVal, a[i][0] + a[otherMedInd][0])

#     print(maxVal)


def solver(n, k, a, b):
    for i in range(n):
        a[i] = (a[i], b[i])
    a.sort()
    medInd = (n-1)//2
    maxVal = float("-inf")

    


    print(maxVal)

def takeInputAndPutItInSolver():
    
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    solver(n, k, a, b)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()