def resolve():
    '''
    code here
    '''
    import collections

    H, W = [int(item) for item in input().split()]
    N = int(input())
    As = [int(item) for item in input().split()]

    grid = [[0 for _ in range(W)] for _ in range(H)]

    def paint(num,i, j, tiles):
        #　iを偶奇で訳て向きを書て塗っていく　そうするとつながる

        return


    cnt = 0
    for i in range(W):
        for j in range(H):
            if grid[i][j] == 0:
                paint(cnt, i, j, As[cnt])
                cnt += 1
                break

            if cnt == N:
                break
    
    for line in grid:
        print(line)

if __name__ == "__main__":
    resolve()
