def resolve():
    '''
    code here
    '''
    import collections
    K = int(input())

    que = collections.deque(list(range(1,10)))

    cnt = 0
    
    while cnt < K:
        cnt += 1
        temp = que.popleft()

        push1 = temp*10 + temp%10 - 1
        push2 = temp*10 + temp%10
        push3 = temp*10 + temp%10 + 1

        if temp%10 != 0:
            que.append(push1)
        
        que.append(push2)

        if temp%10 != 9:
            que.append(push3)
        
    print(temp)



if __name__ == "__main__":
    resolve()
