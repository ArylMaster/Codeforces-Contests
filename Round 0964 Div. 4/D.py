def solver(s, t):
    m, n = len(s), len(t)
    if m < n:
        print("NO")
        return
    
    string = []
    i = j = 0

    while i < m and j < n:
        if s[i] == t[j]:
            string.append(s[i])
            j += 1
        elif s[i] == '?':
            string.append(t[j])
            j += 1
        else:
            string.append(s[i])
        
        i += 1

    if j != n:
        print("NO")
        return
    
    for k in range(i, m):
        if s[k] == '?':
            string.append('a')
        else:
            string.append(s[k])

    print("YES\n" + ''.join(string))


def takeInputAndPutItInSolver():
    # int(input())
    # list(map(int, input().strip().split()))
    s = input()
    t = input()
    solver(s, t)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()