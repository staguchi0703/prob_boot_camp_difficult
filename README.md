# 解説
# 解法

## 方針

* 二重ループで条件に合うものをリスト化する
* ?部をaに置き換える
* 辞書順に並び替えて最初を選ぶ


## 実装

* 同じ部分があるか探すときに、検索範囲外の前方を足しておいた
  * 結局検索範囲外の後方を足さなければならないので、敢えてループの中で操作する必要はないことに後で気が付いた
* 理想的には、
  * 検索範囲で合致を見つけたのち、前方と後方を足してリストに積めば良かった。
  * 最初後方を積み忘れてていてWAを連発していた。これの回避策にもなる


# 別解

## 方針

* 辞書順で?はaに置き換わるのだかからなるべく後方の文字とTを一致させたい。
* だったら最初から入力をさかさまに受けておいて、最初に合致したものが解とすればよい。
  * なるべく？を前方に残したものを解とする　→　辞書順の特徴を利用する。


## 実装

* 逆向きに積むので混乱しやすいので注意
* 入力を全て逆に受けて、最初に見つけた解を答えとするに徹することで、ミスを防げる。
* 今回の解法は検索範囲の前方と検索範囲中も順に積んでいったが、前方も検索範囲も検索が確定した時点で積む文字は決まっているので、検索と文字列の作成は分けた方が混乱防止の観点でよい。
* 今回も最初後方の積み擦れによりWAを連発していたので注意。
  * 検索と文字列作成の機能分離を意識する事が間違えない為に重要。



## 方針

* 一番大きい数から順にN個はひっくり返されない。
* よって、クエリの大きい数を順に最大N個用意する
* 元の整数列を並び替えてクエリから用意した数列と比較して大きいほうの数だけ残す

## 実装

* 並べて比較すればいいだけなのでなんともなかった。。。
  * Dは降順
  * A_listは昇順で比較した


# 失敗解

## 方針

* クエリが$10^5$でどこに入れたらいいかはbisctで$O(logN)$だからいけると思った。
* 区切りを見つけてスライスで処理すれば$O(1)$かと思ってたのが間違い
  * 範囲スライスすれば抜き出した個数文の時間が書かかる
  * 結局N個のリストにしているから$O(N^2)$かかっていた



## 方針

* RLの境界に集まってくるので、ランレングス圧縮する
* LRの境界は離れていくのでここを区切りにできる
* R...L...の塊で考える
* 10*100回は偶数だから十分回数移動したときの偶数配置を考える
* RRR[R]LLLLの[R]から見ると、距離偶数個の物が集まってくる
* RRRR[L]LLLの[L]から見ても、距離偶数個の物が集まってくる

## 実装

* ランレングス圧縮のライブラリがあれば使うのが簡単だが、見つからなかったので実装した。
  * forで回すと最後のLが区切り判定されないので、最後の文字を忘れないように圧縮する必要がある。
* 自分の位置に集まってくる文字の数え方
  * RとLの数が変わるので工夫が必要
  * 自分からみた自分と同じ文字はN-1個、違う文字はN個と数えて偶数距離の個数を数える必要あり。


# 別解
* ダブリングで計算量を抑えた解法ができるらしいが、解の求め方が分からなかった。
* サンプルはACするが途中で死ぬ
  

# 解法

## 方針

* H,W <= 20だからBFSで全点開始しても$O((HW)^2) = 1.6 \cdot 10^5$なので余裕で間に合う
* 最短距離の最長を求めたいので、BFSの最短経路を訪問済みノードに記録する

## 実装

* 定石どおりにqueは`collections.deque()`を使う。
* 注意ポイント
  * queに座標と順序（経過時間）両方入れてしまうと処理時間が大幅に長くなってしまう。
  * このフォルダの`sample_code.py`で検証できる。
  * queに追加するのは次の座標情報に留めるべき。
  * NGコード`que.append([x, y, cnt])`
* 今回は訪問済み座標を記録する必要があったので、そこに順序（経過時刻）を記録する。


## 方針

* 前後桁の差が1以内の整数を求めるので、1桁目に対して2桁目を選んで決められる
* このように前の情報から次の値を予測する方法ではqueを使うと効果的
* また、求める整数は前の情報の下一桁を加えた数と±1になる。
* つまり、前の情報は±1に対して10倍のレンジで変わるため順序が入れ替わることがない。
* ただし、求める数の中心値の下一桁が0との時に-1すると繰り下がりで上位桁の値が変わってしまって、求める整数の条件を満たさなくなるため、条件分岐する必要がある。
* 同じく、求める数の中心値の下一桁が9の場合に+1すると繰り上がりで同様の不具合が発生するため、条件分岐の必要あり。

## 実装

* 当たり前すぎるけど難しく考えていると忘れがちな下記を使う
  * 下一桁の値を調べるには`num%10`
  * 桁をシフトするには`num*10`


## 方針

* 一つを固定する
* 0に固定すると計算が容易
* S=10**9だから、`(10**9, 1)` も固定する
* `y2 = (S+x2)/10**9`のy2とx2が整数の時
  * `x2 = (10^9 - S%(10-^9))%10^9`
    * x2=10^9の時は0


## 実装

* 割り算の商と積を求めるにはdivmod()


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


# 実直にSIMする解法

## 方針

* 隣り合う数値の差が最大になるだから、並び変える際に常に差分が最大になるようにおいていく。
* 与えられた数列を順番に並び変えて`A_ordered = collection.deque()`で保持する
  * 頭＝最小値とお尻＝最大値の取り出し処理が早くで容易



## 実装

* 最初に最大値と最小値を抜き出し並べた`res_list = collection.deque()`を用意する
* その差の絶対値を暫定解`res`とする
* `res_list`の頭とお尻と`A_ordered`の頭とお尻（残りの最大と最小）をそれぞれ4通りの組み合わせで比較して、差の絶対値が最大になるように、`res_list`に値を並べていく。
* 並べ替えと同時に`res`を積算していく

# 数式から導かれる解法

## 方針


* 解の数列を$|a_i|$とすると、小、大、小、大、と並ぶので、解の求め方は以下となる
  * $(a_2 -a_1) + (a_2 - a_3) + (a_4 -a_3) + ... +(a_i - a_{i-1})もしくは(a_{i-1} - a_i)$　…式１
  * $-a_1 + 2a_2 -2a_3 + .... +a_iもしくは-a_i$　…式２
* よって与えられた数列の大きいものと、小さいものから順に係数2へ割りあててゆき、最後に残った二つ（真ん中の二つ）の値を$a_1$と$a_i$に当てる。
* 上記割り当てが決まれば、式２を計算するのみ。
* 数学的な考察が出来れば実装は簡単
* 差が最大（最小に）になる数列の問題は多く出るので、解の数学的な考察は覚えておいた方がよさそう。

## [ABC148E](https://atcoder.jp/contests/abc148/tasks/abc148_e)


### 解法

* 定義より奇数は10が作れないので必ず0が0個
* 0の数は10の数が何個数列の中にあるか
* 10の数は5の倍数の数
  * 数列の要素は全て2の倍数のため、5があれば他のふんだんにある2との組み合わせで10が作れる

### 実装

* 工夫なし

## [ABC054B-B - Template Matching](https://atcoder.jp/contests/abc054/tasks/abc054_b)

### 解法

* 全探索

### 実装

* 受け取った値をリストで持つのか文字で持つのかで書き方が変わる
  * うっかりバグらせるとハマるので注意
  * もしバグったら最初に疑った方がいいかも


  ```python
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]
  ```

  ```python
    A = [[item for item in input()] for _ in range(N)]
    B = [[item for item in input()] for _ in range(M)]
  ```

  * 配列の区間をしていするときに`A[i:i+n][j:j+m`としたくなるがNGなので注意
  * `A[i:i+n]`の時点で要素は減っているが次元が減っていないので`[j:j+m]`しても同じ次元のスライスに行くだけ
    * 書くなら右　→　`small_grid = [line[j:j+M] for line in A[i:i+M]]`


## [ABC130D](https://atcoder.jp/contests/abc130/submissions/14716464)
 
* 尺取り法も二分探索も実装出来ない
* しばらくたってもう一回

## [nikkei2019-2-qual](https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b)

### 解法

* 気が何通りできるか？は、今見ているノードの親は何通り選べるか？を考える。
* 今見ているノードの距離から親のノードの個数は？
  * 親ノードには何個ぶらさがっても良いから、親ノード候補の数だけ場合がある
  * 他のノードと重複しようが関係ない
* ルート以外のノードで親のノード数をかけ合わせればよい

### 実装

* とくに工夫なし


## [sumitb2019_d](https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d)

### 貪欲法

#### 解法

* 暗号は高々000-999なので全通り試せばよい
* 与えられた数字の頭から順に合致するものを探す

#### 実装

* 000とか002を作るのに0埋めを使う
  * `'{:0>3}'.format(num)`
  * `>`が数字の右寄せ（0を左から埋める）

### 動的計画法

#### 解法

理解不能


## [ABC057C](https://atcoder.jp/contests/abc057/tasks/abc057_c)

### 解法

* 最小で分割すると、$\sqrt{N}$だが、整数にできるかが問題
* バカでかい素数をNに与えられる事も考えると、$\sqrt{N}$以下のNを割り切れる整数を探す必要がある。
  * 答えは1かもしれない
* 上記整数が分かれば、その桁とNを割った桁を求めて大きいほうが解
  
* 実直に素因数分解して、因数最大限偏らないようにAとBを作ったが、一問WAしていた原因は分からない。

### 実装

* 特になし

## [ABC107C](https://atcoder.jp/contests/abc107/tasks/arc101_a)

### 解法

* 連続区間をとる
* 右端か左端が０に近いほうから連続区間をとった方が最小となる
* 右端から計上した場合と、左端から計上した場合と両方を計算しておく
* N個のうちK個選ぶから、N-k+1通りの連続区間の選び方ができる