def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    grid = [[int(item) for item in input()] for _ in range(N)]
    res_grid = [[0 for _ in range(M)] for _ in range(N)]

    def search(i, j, grid=grid):
        return min(grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1])


    def fix(i, j, a, res_grid=res_grid, grid=grid):

        grid[i-1][j] -= a
        grid[i+1][j] -= a
        grid[i][j-1] -= a
        grid[i][j+1] -= a
        res_grid[i][j] += a

        return [grid, res_grid]

    is_found = False
    for i in range(1, N-1):
        for j in range(1,M-1):
            # print(i,j)
            grid, res_grid = fix(i,j, search(i,j))

    for line in res_grid:
        line = [str(item) for item in line]
        print(''.join(line))

if __name__ == "__main__":
    resolve()
