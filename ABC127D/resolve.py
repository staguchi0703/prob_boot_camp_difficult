def resolve():
    '''
    code here
    '''
    import bisect
    import collections
    N, M = [int(item) for item in input().split()]
    A_list = [int(item) for item in input().split()]
    queries = [[int(item) for item in input().split()] for _ in range(M)]
    queries = sorted(queries, key=lambda x:x[1], reverse=True)
    A_list.sort()

    cnt_b = 0
    D = collections.deque()
    for i in range(M):
        b, c = queries[i]
        cnt_b += b
        for _ in range(b):
            D.append(c)
        if cnt_b >= N:
            break
    D_len = len(D)
    res = 0
    for i in range(N):
        if i < D_len:
            res += max(D[i], A_list[i])
        else:
            res += A_list[i]

    # print(A_list)
    print(res)




if __name__ == "__main__":
    resolve()
