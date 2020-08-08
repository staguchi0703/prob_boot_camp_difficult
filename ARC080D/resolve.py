def resolve():
    '''
    code here
    '''
    H, W = [int(item) for item in input().split()]
    N = int(input())
    As = [int(item) for item in input().split()]

    line = []
    for i, val in enumerate(As):
        line += val * [i+1]

    grid = [[] for _ in range(H)]

    for i in range(H):
        if i % 2 == 0:
            grid[i] = line[i*W: W*(i+1)]
        else:
            grid[i] = line[i*W: W*(i+1)][::-1]

    for temp in grid:
        print(*temp)

if __name__ == "__main__":
    resolve()
