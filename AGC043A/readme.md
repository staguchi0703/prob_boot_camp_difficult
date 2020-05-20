# 解法

## 方針

* 経路中の黒の個数をDPで求める
* DPの漸化式が分からなかった

## 参考
* [黒色(障害物みたいなもの)が繋がってたら、1回の「操作」で白色(道)に変えられる！

ということです！](https://qiita.com/rudorufu1981/items/0e2332614a4f7879a849)


### 参考コード

``` AGC043A.py
def LI(): return list(map(int,input().split()))
H,W = LI()
S = [input() for _ in range(H)]
dp = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        judge = 1 if S[i][j]=='#' else 0
        if i==0: #0行目
            if j==0:
                dp[0][0] = judge
            else:
                dp[0][j] = dp[0][j-1]+judge*(0 if S[0][j-1]=='#' else 1)
        else: #0行目以外
            if j==0:
                dp[i][0] = dp[i-1][0]+judge*(0 if S[i-1][0]=='#' else 1)
            else:
                temp1 = dp[i][j-1]+judge*(0 if S[i][j-1]=='#' else 1)
                temp2 = dp[i-1][j]+judge*(0 if S[i-1][j]=='#' else 1)
                dp[i][j] = min(temp1,temp2)
print(dp[-1][-1])
```