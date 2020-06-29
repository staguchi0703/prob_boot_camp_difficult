def resolve():
    '''
    code here
    '''

    N, M = [int(item) for item in input().split()]
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    is_found = False
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_grid = [line[j:j+M] for line in A[i:i+M]]
            # print(temp_grid)
            if B == temp_grid:
                is_found = True
                break
        if is_found:
            break

    print('Yes') if is_found else print('No')

if __name__ == "__main__":
    resolve()
