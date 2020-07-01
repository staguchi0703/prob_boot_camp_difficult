def resolve():
    '''
    code here
    '''
    import math
    N = int(input())
    sqrt_n = math.sqrt(N)

    B1=10**10
    for i in range(1, int(sqrt_n)+1):
        if N % i == 0:
            B1 = min(B1, N//i)
            
    B2 = N // B1
    print(max(len(str(B1)), len(str(B2))))


if __name__ == "__main__":
    resolve()
