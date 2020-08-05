def resolve():
    '''
    code here
    '''
    import collections

    H, W = [int(item) for item in input().split()]
    N = int(input())
    As = [int(item) for item in input().split()]

    grid = [[0 for _ in range(W)] for _ in range(N)]

    def paint(num,i, j, tiles):
        # bfsの考えでtiles個塗っていく
        que = collections.deque([[i,j]])

        return


    cnt = 0
    for i in range(W):
        for j in range(H):
            if grid[i][j] == 0:
                paint(cnt, As[cnt])
                cnt += 1
                break

            if cnt == N:
                break
    
    for line in grid:
        print(line)

if __name__ == "__main__":
    resolve()
