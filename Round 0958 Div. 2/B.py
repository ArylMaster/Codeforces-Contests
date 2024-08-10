from collections import deque

def solver(n, a):
    if n == 1:
        if a == '1':
            print('YES')
        else:
            print("NO")
        return

    q = deque()
    for i in a:
        if not q:
            q.append(i)
        else:
            if i == '1':
                q.append(i)
            else:
                if q[-1] != '0':
                    q.append(i)

    ones = 0
    zeros = 0
    for i in q:
        if i == '1':
            ones += 1
        else:
            zeros += 1

    if ones > zeros:
        print("YES")
    else:
        print("NO")



def takeInputAndPutItInSolver():
    n = int(input())
    # list(map(int, input().strip().split()))
    a = input()
    solver(n, a)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()