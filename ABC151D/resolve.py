def resolve():
    '''
    code here
    '''
    import collections
    H, W = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    res = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':

                que = collections.deque([[i,j]])
                footprint = [[-1 for _ in range(W)] for _ in range(H)]
                footprint[i][j] = 0

                while que:
                    a, b = que.popleft()
                    c = footprint[a][b]
                    if c > res:
                        res = c

                    if a != 0 and footprint[a-1][b] == -1 and grid[a-1][b] == '.':
                        que.append([a-1, b])
                        footprint[a-1][b] = c + 1
                    if a != H-1 and footprint[a+1][b] == -1 and grid[a+1][b] == '.':
                        que.append([a+1, b])
                        footprint[a+1][b] = c + 1
                    if b != 0 and footprint[a][b-1] == -1 and grid[a][b-1] == '.':
                        que.append([a, b-1])
                        footprint[a][b-1] = c + 1
                    if b != W-1 and footprint[a][b+1] == -1 and grid[a][b+1] == '.':
                        que.append([a, b+1])
                        footprint[a][b+1] = c + 1

    print(res)
        


if __name__ == "__main__":
    resolve()
