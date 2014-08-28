# mincut.py

与えられた重み付き有向グラフの最大フローおよび最小カットを求める。  
アルゴリズムは [Edmonds-Karp][Edmonds-Karp] のアルゴリズムです。  

## 注意！

このプログラムはお勉強のために実装したものであり、実用レベルではありません！  
実際に cut したい人は [これ][Kolmogorov] とか使うとよいと思います。  
激はやです。

## 関数

    f, F = stmaxflow(s, t, C)

有向重み付きグラフ C の s-t maxflow を求める。  
f は得られた maxflow。  
F は得られたエッジ毎の流量。  

    f, c = stmincut(s, t, C)

有向重み付きグラフ C の s-t mincut を求める。  
f は得られた mincut (= カットされたエッジの重みの総和) = maxflow。  
c はカット後に各節点がソース側、シンク側のどちらに属するかを表すベクトル。  

    f, c = mincut(C)

有向重み付きグラフ C の mincut を求める。  
mincut では s,t を指定せず、micut を最小化する s, t を自動的に選ぶ。  
f, c は stmincut と同様。

    f, c = kmincut(C, k)

有向重み付きグラフ C の k-mincut を求める。  
k-mincut では mincut を k-1 回行うことで節点を k 個のグループに分割する。  
f は mincut の総和。  
c は各節点の所属ベクトルである。


## サンプルコード

main.py は標準入力で有向グラフを受け取り、最小カットを計算する。

### 入力

入力の重み付き有向グラフは以下の形式のファイルで与えられる。  
ちなみに以下のネットワークは [wiki][wiki] のやつです。

    7
    0 1 3
    0 3 3
    1 2 4
    2 0 3
    2 3 1
    2 4 2
    3 4 2
    3 5 6
    4 1 1
    4 6 1
    5 6 9

1行目は節点数、2行目以降は辺の始点、終点、重みである。  

### 出力

例えば上記のファイルを入力とすると以下の出力を得る。

    $ cat wiki.txt | ./main.py
    1.0
    [4 6]
    [0 1 2 3 5]

1行目は得られた mincut。  
2, 3行目はカット後の節点のグループを表す。


[Edmonds-Karp]: http://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%89%E3%83%A2%E3%83%B3%E3%82%BA-%E3%82%AB%E3%83%BC%E3%83%97%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0 "Edomonds-Karp"
[wiki]: http://ja.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E3%83%95%E3%83%AD%E3%83%BC%E6%9C%80%E5%B0%8F%E3%82%AB%E3%83%83%E3%83%88%E5%AE%9A%E7%90%86 "wiki" 
[Kolmogorov]: http://pub.ist.ac.at/~vnk/software.html "Kolmogorov"
