def resolve():
    '''
    code here
    '''
    sx, sy, tx, ty = [int(item) for item in input().split()]

    gx = tx - sx
    gy = ty - sy

    def r(num):
        return 'R'*num
    
    def l(num):
        return 'L'*num
    
    def u(num):
        return 'U'*num

    def d(num):
        return 'D'*num

    first_trail = l(1) + u(gy+1) + r(gx+1) + d(gy+1) + l(gx)
    second_trail = u(gy) + r(gx+1) + d(gy+1) + l(gx+1) + u(1)

    print(first_trail + second_trail)


if __name__ == "__main__":
    resolve()
