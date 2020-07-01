def resolve():
    '''
    code here
    '''
    import collections
    N, X, Y = [int(item) for item in input().split()]
    X -= 1
    Y -= 1

    edges = [[] for _ in range(N)]
    for i in range(N-1):
        edges[i].append(i+1)
        edges[i+1].append(i)
    edges[X].append(Y)
    edges[Y].append(X)


    fp = [-1 for _ in range(N)]

    res_memo = [0 for _ in range(N)]
    for i in range(N):
        fp = [-1 for _ in range(N)]
        que = collections.deque([[i, 0]])
        fp[i] = 0
        while que:
            node, dist = que.popleft()
            for to_node in edges[node]:
                if fp[to_node] == -1:
                    que.append([to_node, dist+1])
                    fp[to_node] = dist+1

        for item in fp:
            res_memo[item] +=1
    
    for item in res_memo[1:]:
        print(item//2)



if __name__ == "__main__":
    resolve()
