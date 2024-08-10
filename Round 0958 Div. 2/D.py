def solver(n, V, adj):
    if n == 1:
        print( V[0])
        return
    
    visited = [False]*n

    S = [0]
    S1 = [0]
    S2 = [0]

    def DFS(node, s1, s2, S):
        if visited[node]:
            return
        visited[node] = True    
        S[0] += V[node]
        s1[0] += V[node]
        for i in adj[node]:
            DFS(i, s2, s1, S)

    DFS(0, S1, S2, S)

    total = S[0] + min(S1[0], S2[0])
    print(total)

    







    pass

def takeInputAndPutItInSolver():
    n = int(input())
    V = list(map(int, input().strip().split()))
    adj = [[] for _ in range(n)]

    for _ in range(n-1):
        a, b = list(map(int, input().strip().split()))
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    solver(n, V, adj)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()