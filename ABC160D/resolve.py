def resolve():
    '''
    code here
    '''
    import collections
    N, X, Y = [int(i) for i in input().split()]

    edges = [[] for _ in range(N)]
    fp = [0 for _ in range(N)]

    for i in range(N-1):
        edges[i].append(i+1)
        edges[i+1].append(i)

    edges[X-1].append(Y-1)
    edges[Y-1].append(X-1)


    cnt = 0
    for k in range(N-1):
        for i in range(N):
            que = collections.deque([edges[i]])
            dist = 0
            while que:
                temp = que.popleft()
                dist += 1
                if dist == k:
                    cnt += 1
                    que = False
                else:
                    print(temp)
                    # for j in temp:
                    #     if fp[j] != 1:
                    #         que.append(j)
                    #         fp[j] = 1
    print(cnt)


if __name__ == "__main__":
    resolve()
