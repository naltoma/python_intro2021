# ループ処理

## iteration (繰り返し処理)とは
```{figure} ./figs/iteration.svg
:name: iteration
繰り返し処理を使いたい状況
```

これまでに学んできたプログラムにおける処理の流れは、コードを上から順序通りに実行する逐次処理と、条件式に基づき処理すべきブロックを移動する条件分岐がある。基本的にはこれらの組み合わせであらゆるプログラムを記述できるが、(1)ある処理を指定回数繰り返したり、(2)ある集団に対して同じ処理を適用するようなコードを書く際に不便である。例を見てみよう。

```python
# (1) ある処理を指定回数繰り返したい。
# 全く同じ命令を指定回数列挙するだけで良いが、回数毎に書き直すのは不便。
print('ガチャを1回引きました！')
print('ガチャを1回引きました！')
print('ガチャを1回引きました！')
print('ガチャを1回引きました！')

# (2) ある集団に対して同じ処理を適用したい。
# 一部分だけ異なるが、プレイヤー毎に書き直すのは不便。
print('勇者1は経験値10を得た！')
print('勇者2は経験値10を得た！')
print('勇者3は経験値10を得た！')
print('勇者4は経験値10を得た！')
```

上記のようにコードとして書くことは可能だが、何らかの理由でその命令文を修正したい場合には全ての命令文を修正する必要があるし、過不足なく指定回数書いたかどうかを確認することは手間がかかる。

これらの理由から、一般的にプログラミング言語においては「ある一定回数繰り返させたい」場合の処理を **{index}`ループ処理<るーぷしょり-ループ処理>`や{index}`繰り返し処理<くりかえししょり-繰り返し処理>`（{index}`looping`, {index}`iteration`）** と呼び、専用の予約語を用いて記述することが多い。Pythonにおいては ``for``, ``while`` の2種類の書き方が提供されている。まずfor文について学んでみよう。

---
## for文の例1
```{figure} ./figs/for1.svg
:name: for1
for文の例1
```

{index}`for文`は ``for 変数 in シーケンス:`` という記述で書き始める。forと変数、変数とin、inとシーケンスの間は半角スペースが必要だ。

**{index}`シーケンス<しーけんす-シーケンス>`（{index}`sequence`）** とは「順番の付いた集合」である。例えば、順番を考慮せず単に集合として「りんご、みかん、バナナ、、、」と果物を集めたものはシーケンスではない。これに対し「1番目にりんご、2番目にみかん、、、」のように順番が付いて並べられているものをシーケンスと呼ぶ。上記のコードでは ``range(4)`` がシーケンスに相当する。{index}`range関数`の中身を確認するためには一度 **{index}`list型`** に変換すると分かりやすい。次のように実行してみよう。
```python
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
```
最初のコードがrange関数の結果であり、その結果は ``range(0,4)`` と出力されている。これは **{index}`range型オブジェクト`** と呼ばれ、そのままでは中身が分かりにくい。この中身を確認しやすくしたのが次の ``list(range(4))`` である。``[]`` は ``list型`` と呼ばれており、中身が ``0, 1, 2, 3`` とint型リテラル0から3まで、合計4個の要素が並んでいる。List型は後日改めて確認するため、ここでは「range関数で引数を自然数kで指定して実行すると、0〜k-1の数字が並んで用意される」ことを覚えよう。

```{note}
世の中では順番を付けて処理する際には「1番目、2番目、、」として1番目から数えることが多い。これに対してプログラミングの世界では、多くの場合0から数える。これはプログラミング言語の慣習のようなものとして覚えておこう。
```

さて、range関数を用いてシーケンスを用意した。このシーケンスに対して、頭から一つずつ要素を取り出し、ブロック内の処理を実行するのがfor文である。Range関数で用意したシーケンスは「0, 1, 2, 3」であるため、最初の値は「0」だ。この値が変数 i に保存された状態でブロック内の処理が実行される。このため、その次は実行させたいブロックを、if文でも書いたようにインデントで指定してコードを書く必要がある。上記コードの例では print(i) となっており、変数iには0が保存されているため、最初は0が出力される。

ここでブロックは終わるため、for文はシーケンス内の次の値を確認する。次の値はint型リテラル1であり、これを変数iに保存してブロック内のコードを実行する。以下同様に、ブロック内のコードを処理し終えると次の値である2を変数iに保存してブロック内のコードを実行する。さらに、ブロック内のコードを処理し終えると次の値である3を変数iに保存してブロック内のコードを実行する。3に対する処理まで実行し終えると、シーケンスに残された値はなく、全ての値に対する実行をし終えていることが分かる。このようにシーケンス内全ての値に対して実行し終えると、for文を終了する（ブロックを抜けて、その下のコードに移動する）ことになる。ここではその下にはもうコードはないため、ここで動作終了となる。

```{note}
for文で ``in range(5):`` のように書かれると ``in [0, 1, 2, 3, 4]`` と同等の実行をする。つまりrange関数は1からではなく0から数えるが、結果的には指定された回数分だけループブロック実行しろという命令になる。つまり一定回数繰り返したい場合には for文 + range関数 の組み合わせが便利だ。
```

---
## for文の例2
```{figure} ./figs/for2.svg
:name: for2
for文の例2
```

例1で見た通り、for文はシーケンスに対して一つずつ要素を取り出して、処理を実行する。そのシーケンスを表現するためによく使う型がlistである。listは他のオブジェクトを何でも並べて列挙することができる。

上記コード例では、1番目にint型リテラル80を、2番目にint型リテラル60を、3番目にint型リテラル50を、4番目にstr型リテラルhogegeをカンマ（,）で区切って列挙している。それら全体を ``[`` と ``]``で囲うことでlist型オブジェクトを作成している。なお、ここでは分かりやすいように「1番目」から数え上げたが、Pythonのlistや他の多くの言語における配列と呼ばれるオブジェクトにおいては、殆どの場合「0番目」から数える。例えば次のように実行すると何が出力されるか確認してみよう。
```python
scores = [80, 60, 50, 'hogege']
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4]) # IndexError: list index out of range
```
変数scoresの中に上記コード例1行目のように保存した後で、scores[0] をprint関数で出力させると、80が出力されるはずだ。このように0番目から数え始め、最後は scores[3] に 'hogege' が保存されている。

```{tip}
上記の例で ``scores[4]`` を参照しようとすると「{index}`IndexError`: list index out of range」という応答が返ってくる。これは指定したリストscoresの範囲外のインデックス4が指定されたというエラーだ。scoresは4つの要素を持つリストであるが、各要素は0番目から数えるため最後は3番目までしか存在していない。そのため4番目を指定すると IndexError となる。
```

`````{admonition} 検討1
3つの課題に対する採点結果を ``scores = [50, 100, 80]`` として用意したとしよう。このリストを引数として受け取り、総合得点を求める関数を実装してみよう。関数名を get_total_score とする。
````{dropdown} 回答例
```python
def get_total_score(scores):
    result = 0 # 総合得点を保存しておくための変数。初期値は0。
    for score in scores:
        result += score
    return result

#動作確認
scores = [50, 100, 80]
print(get_total_score(scores))
print(get_total_score([1, 2, 3]))
```
````
`````

`````{admonition} 検討2
3つの課題に対する採点結果を ``scores = [50, 100, 80]`` として用意したとしよう。このリストを引数として受け取り、平均点を求める関数を実装してみよう。関数名を get_average_score とする。
````{dropdown} 回答例
```python
def get_average_score(scores):
    total = 0 # 総合得点を保存しておくための変数。初期値は0。
    count = 0  # 何回分の点数が保存されていたかをカウントするための変数。初期値は0。
    for score in scores:
        total += score
        count += 1
    result = total / count
    return result

#動作確認
scores = [50, 100, 80]
print(get_average_score(scores))
print(get_average_score([1, 2, 3]))
```
````
`````

---
## while文の考えかた
```{figure} ./figs/while1.svg
:name: while1
while文の考え方
```

for文とは別のループ文、while文について学んでみよう。

for文ではリストのように順序付けられた要素集合（シーケンス）を用意した上で、一つずつ要素を取り出してループブロックを実行する。これに対し{index}`while文`では、**ある条件式を満足している間中ループブロックを実行する** ように動作する。

---
## while文の例1
```python
# 終了条件がないため、実行終了したいなら強制終了(ctrl+c)しよう。
import time

signals = ["🔵", "🟡" ,"🔴"]
i = 0
while(True):
    print(signals[i])
    i += 1
    if( i == 3 ):
        i = 0
    time.sleep(3)
```

上記は[e20の学生](https://twitter.com/rienNeVaPlusOne/status/1370384033176195081)が考えてくれたコードだ。実行すると ``🔵🟡🔴`` が繰り返し出力される。以下コードを解説していく。

- 1行目: ``import time``
  - 時刻を扱うPython標準モジュール [time](https://docs.python.org/ja/3.8/library/time.html) を読み込んでいる。
- 3行目: ``signals = ["🔵", "🟡" ,"🔴"]``
  - リストを用意した。🔵は0番目、🟡は1番目、🔴は2番目。
- 4行目: ``i = 0``
  - 一番最初に🔵を出力し、次に🟡、最後に🔴を出力したら、また🔵に戻るようにしたい。これを実現するためのカウンタとして変数iを利用している。具体的には、
    - iの値が0のときは ``signals[0]``を出力し、その次に向けてiを1に上書きする。
    - iの値が1のときは ``signals[1]``を出力し、その次に向けてiを2に上書きする。
    - iの値が2のときは ``signals[2]``を出力し、その次に向けてiを3に上書きする。ここで signals[3] は存在しないため、iを0に上書きし直す。
- 5行目: ``while(True):``
  - ここで指定された条件式が True ならばループブロックを実行する。ループブロックを実行し終えると再びこの条件式に戻り、チェックされる。今回の例では True bool値を直接書いているため **ループ処理を繰り返し続ける** という意味になっている。
- 6行目: ``print(signals[i])``
  - リストsignalsの指定された要素を出力する。
- 7行目: ``i += 1``
  - カウンタ変数iをインクリメント（1増加）する。
- 8〜9行目: ``if( i == 3 ):``
  - カウンタ変数iが3に等しいならば、0に初期化する。初期化する意図は4行目の解説を参照。
- 10行目: ``time.sleep(3)``
  - 1行目で読み込んだtimeモジュールが持っている[sleep関数](https://docs.python.org/ja/3.8/library/time.html#time.sleep)により、3秒間実行を停止する。
  - ここでループブロックが終わるため、5行目の ``while(True)`` に戻る。

```{note}
{index}`モジュール<もじゅーる-モジュール>`とは便利な機能をまとめたものであり、例えば「数学モジュール[{index}`math`](https://docs.python.org/ja/3.8/library/math.html)」「システムモジュール [{index}`sys`](https://docs.python.org/ja/3.8/library/sys.html)」等がある。これらは{index}`ライブラリ<らいぶらり-ライブラリ>`（図書館）と呼ばれることも多く、必要に応じて必要なモジュールやライブラリを読み込んで利用する。事前にあらゆるモジュールを読み込んでしまうといくらメモリがあっても足りないため、このように「読み込んで利用する」という手順をとっている。
```

```{note}
{index}`インクリメント<いんくりめんと-インクリメント>`({index}`increment`)では ``+=`` 演算子を使って記述した。同様に ``-=, *=, /=`` も用意されている。特に ``i -= 1`` のように1減らす処理は{index}`デクリメント<でくりめんと-デクリメント>`({index}`decrement`)と呼ばれる。
```

```{warning}
無限ループに陥ってしまった場合、プログラムを強制終了する必要がある。強制終了するには **{index}`Ctrl+c`** を入力しよう。
```

`````{admonition} 検討
信号機のコード例を参考にし、青が3回出力したら終了するようにコードを修正せよ。なお開発中は円滑にするためtime.sleepをコメントアウトして構わない。
````{dropdown} 回答例
```python
import time

signals = ["🔵", "🟡" ,"🔴"]
i = 0
blue_count = 0
while(True):
    print(signals[i])
    if signals[i] == "🔵":
        blue_count += 1
        if blue_count == 3:
            break
    i += 1
    if( i == 3 ):
        i = 0
    time.sleep(3)
```
````
`````

---
## while文の例2
```python
# スライムのHPが0より大きい間タコ殴りにするゲーム
import random

def encount_enemy():
    hitpoint = random.randint(3, 7)
    return hitpoint

hp = encount_enemy()
print('敵に遭遇した。(敵HP={})!'.format(hp))

while (hp > 0):
    damage = random.randint(2,4)
    hp = hp - damage
    print('敵に{}のダメージ!(敵HP={})'.format(damage,hp))

print('スライムを倒した！')
```

```{note}
このコードから以下のことを読み取れるようになろう。
- どこに関数定義があるのか？
- その関数定義はどこからどこまでなのか？
- 実際に実行されるコードはどこから始まるか？
```

1行目の ``import random`` は [{index}`random`モジュール](https://docs.python.org/ja/3.8/library/random.html) を利用するための宣言文である。

3〜5行目は関数定義の例である。先程読み込んだrandomモジュール内にある関数[randint](https://docs.python.org/ja/3.8/library/random.html#random.randint)を利用して、3〜7の間でランダムに整数を選び、変数hitpointに保存している。このように「モジュール内の関数」を利用する際には **モジュール名.関数名(引数)** のように、**.を使って記述** する必要がある。他にどんな関数があるかはAPIドキュメントを参照してみよう。

7行目は関数を呼び出し、実行している。8行目はその結果をprint出力している。

10行目からがwhile文の例である。条件は「変数 hp が0より大きい」と記述されており、その判定結果が True となる間はループブロックを実行し続ける。言い換えると、条件式がFalseにならない限りCPUやメモリといった計算資源を消費し続けることになる。このような状況（ループから抜け出せなくなっている状況）を、**{index}`無限ループ<むげんるーぷ-無限ループ>`** と呼んだりする。ループブロック内の処理は3行の命令文があり、1つ目は再びrandom.randint()により2〜4の数値をランダムに生成している。その値を用いて変数hpを更新し、次の行でdamage, hpの中身を確認するために出力している。このループブロック内で、変数hpを更新する命令文がどこにも無い場合、もしくは更新するが絶対にループ終了条件を満足しない場合には、無限ループに陥ってしまう。

```{note}
上記コードで「変数hpが0になったら死亡したとみなしてループを抜ける」というコードを書くつもりで ``while (hp == 0)`` と書いてしまうと、**たまに** 想定外のことが起きてしまう。確認してみよう。
```

---
## continue, break
for文ではシーケンスに対する全ての要素に対して処理を行い、while文では条件式を満足している（Trueである）間処理を行う。これに対し、ある特定の場合には処理をスキップして次の要素に移りたいという状況がある。

```python
# continue例
# レポート出した人（0点以外）の平均点を出したい。
scores = [80, 100, 0, 60]
sum = count = 0    # countはレポートを出した人数
for score in scores:
    if score == 0:
        continue
    sum += score
    count += 1

average = sum/count
print(sum, count, average)    # -> 240 3 80.0
```

上記コード例は、「レポートの平均点を、0点を除いて算出したい」という例である。複数人の点数がscoresに保存されており、for文でscoreに一つずつ点数を保存した状態でループブロックを実行する。この際、scoreが0と等しい場合には continue 文が実行される。**{index}`continue文`が実行されるとその後の同一ループブロックを処理をスキップし、ループブロック冒頭に戻り、次の要素の処理に移行** する。

同様のコードはcontinue無しでも記述可能（考えてみよう）である。しかしこちらが書きやすいもしくは読みやすいコードで記述しやすいことがあるため、continue文が用意されている。

```python
# braek例
# レポート出した人（0点以外）の平均点を出したい（バグ有り）
scores = [80, 100, 0, 60]
sum = count = 0    # countはレポートを出した人数
for score in scores:
    if score == 0:
        break
    sum += score
    count += 1

average = sum/count
print(sum, count, average)    # -> 180 2 90.0
```

上記の例も0点を除いて平均点を算出したいコードを書こうとした例であるが、実際には不適切な処理をしている。

{index}`break` は、continue同様にループブロックの処理を操作するための命令である。continueは残りのブロックをスキップし次の要素に移行する。これに対して **breakは、ループブロック全てをスキップする（抜け出す＝breakする）** という動作を行う。このため、上記コードでは80点、100点まではループ処理を行うが、scoreが0になった状態でループ処理を行うとbreakが実行され、シーケンス内の60点は処理されないままfor文を抜け出す。このため、平均点が90点というおかしなことになっている。

この例はbreakが悪いという話ではなく、breakの動作を例示するだけである点に注意すること。ループ処理の際にcontinue, break を使うことで書きやすくなるもしくは読みやすくなることがあるため、命令文として用意されている。

---
## ループ文の入れ子
```python
# 入れ子の例1
for i in range(2):
    for j in range(3):
        print(i, j)
```

上記はループ文が入れ子構造になっているコード例を示している。どのように出力されるか想像できるだろうか。[デバッグ実行](./debug)で1行目にブレイクポイントを設定し、step in実行すると実行行がどのように移動するのか、その最中の変数がどのように変わっていくのかを確認しやすい。

---
## 復習・予習
- 復習
  - 適宜過去資料及び教科書を参照しよう。
- 予習
  - 5.1 Tuples
  - 5.3 Lists and Mutability
  - (5.6 Dictionaries) ＊余裕があれば
