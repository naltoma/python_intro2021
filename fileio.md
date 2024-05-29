# ファイル入出力の基本
教科書「Chapter 4.6 Files」の補足。

---
## 概要
- {index}`File I/O` = File Input/Output
  - 「ファイル、アイ、オー」と呼び、ファイルに対する読み書き操作のことを指す。
- ソースコードとは別に用意されたファイルを利用（ファイルを読み込む、ファイルへ書き込む）する方法を学ぶ。
  - Step1: 「{index}`ファイルハンドラ<ふぁいるはんどら-ファイルハンドラ>` ({index}`file handle`)」を準備する。ファイルオブジェクトとも呼ばれる。
  - Step2: ハンドラに対して読み書きする。
  - Step3: 読み書きし終えたらハンドラを閉じる。

---
## コード例1：書き込み
ファイルへ書き込むコード例を眺めてみよう。

```Python
filename = 'test.txt'
with open(filename, 'w') as fh:
    name = input('あなたの名前は何ですか？ => ')
    fh.write(name + '\n')
print('ファイル書き込み終了')
```
- コード概要
  - 1行目: ``filename = 'test.txt'``
    - 書き込むためのファイル名を設定している。
  - 2行目: ``with open(filename, 'w') as fh:``
    - [{index}`open関数`](https://docs.python.org/3/library/functions.html#open)は、ファイルを開き、そのファイルを処理するためのファイルハンドラを返す関数だ。``'w'``は、ファイルを書き込み(write)モードで開くという指定である。読み込みたい場合には``'r'``を指定する。
    - ``with open() as fh:``は、(1)ファイルをopen()で開き、(2)そのファイルハンドラをfhという変数に保存する。(3){index}`with`ブロック内で、fhに対する処理を記述し、(4)ブロックを抜けると、自動的にファイルを閉じる（ちゃんと保存する）。
      - with構文を使わずに書くことも可能だ。教科書にある最初のコード例がそれだ。この場合には、前述(4)の ``fh.close()`` を記述し忘れることがあり、また、これだけだと様々な理由での例外時の処理をしてくれないことから、with構文の利用を推奨している。
  - 3行目: ``name = input('あなたの名前は何ですか？ => ')``
    - input()は、プログラム実行者からの入力を受け付けたい場合に利用できる関数だ。helpやpydocで調べてみよう。
  - 4行目: ``fh.write(name + '\n')``
    - ``fh.write()``は、指定したファイルハンドラ（fh）に対して、書き込むための関数だ。単に ``fh.write(name)``でも書き込み可能。この場合には「名前」のみ書き込むことになる。ここでは単に改行も加えたい（例えば複数人の名前をループ処理して取得したい場合には改行加えて列挙したい）という意図で、最後に ``\n`` を追加している。
  - 5行目: ``print('ファイル書き込み終了')``
    - withブロックを抜けているため、ここでは既にfh.close()が自動的に実行された後である。fhに対する処理をすることはできない。更にファイル操作したいなら、もう一度openし直す必要がある。

```{note}
- ファイル操作時の注意
  - open()時の代表的なオプションは、{index}`read` 'r', {index}`write` 'w', {index}`append` 'a' あたり。'w'は、「上書きモードで開く」点に注意。もし既にファイルの中身が存在している場合には、中身を削除した上で書き込むことになる。
- ファイルハンドラ名
  - ``with open() as fh:`` は、{index}`ファイルハンドラ<ふぁいるはんどら-ファイルハンドラ>`を変数fhに保存して操作する。fhは file handler の略字として書いているだけであり、``with open() as hoge:`` であれば変数hogeにファイルハンドラが保存される。
```

```{tip}
- openの戻り値は{index}`stream型`オブジェクト。
  - 上記では教科書に合わせて「ファイルハンドラ」として説明したが、より正しくは **stream型オブジェクト** を返す。ストリームは、与えられたデータ型（今回はテキストだが、画像や動画の場合にはバイナリとなる）に応じて読み書き操作を提供する。　興味のある人は[Dive into Python3, 第11章 ファイル](https://diveintopython3tojp.blogspot.com/2016/07/11-01.html)に飛び込んでみよう。
```

---
## コード例2：読み込み
中身は何でも構わないので、2〜5行程度のテキストファイルを用意する。そのファイル名を target.txt としよう。target.txtを用意した上で下記コードを実行してみよう。

```Python
filename = 'target.txt'
with open(filename, 'r') as fh:
    line_no = 1
    for line in fh.readlines():
        print(f'{line_no}行目の中身: type={type(line)}, {line=}')
        line_no += 1
print('ファイル読み込み終了')
```
-　コード概要
  - 1行目: ``filename = 'target.txt'``
    - ファイル名の指定。
  - 2行目: ``with open(filename, 'r') as fh:``
    - with構文にて、readモードでファイルハンドラを用意。
  - 3行目: ``line_no = 1``
    - 読み込んだ行数を表示するための変数を用意している。これは行数をカウントする必要がある場合だけ記述する。
  - 4行目: ``for line in fh.readlines():``
    - ファイルハンドラから「1行を1str型オブジェクト」「そのstr型オブジェクトを要素として持つリスト」として読み込む。この要素を変数lineに保存した上で、forブロックで処理していく。
  - 5行目: ``print(f'{line_no}行目の中身: type={type(line)}, {line=}')``
    - [フォーマット済み文字リテラル(f-stringとも呼ぶ)](https://docs.python.org/ja/3.8/tutorial/inputoutput.html#formatted-string-literals)による出力。
    - ちゃんと読み込めてることを確認するために、出力しているだけのコード例。何もない空の行も出力されていることに注意しよう。これは「行末ある改行文字」もそのまま読み込んでいるため。改行文字を取り除きたいなら [{index}`str.rstrip関数`](https://docs.python.org/ja/3/library/stdtypes.html?highlight=split#str.rstrip) を使おう。
  - 6行目: ``line_no += 1``
    - 行番号を更新。
  - 7行目: ``print('ファイル読み込み終了')``
    - withブロックを抜けているため、処理がここに辿り着いた時点でfhに対する処理は終了。

```{note}
- ファイルとプログラムの位置に注意。
  - 上記コードは ``open('target.txt', 'r')`` が実行される。ここで ``target.txt`` は、プログラム実行時のディレクトリ上にあるファイルを探そうとする。もしそこに存在しないのであれば **FileNotFoundError** を返す。
- 読み込んだ個々の値はstr型。
  - 例えばテキストファイルに ``12345`` という5文字が保存されているとしよう。このファイルを1文字ずつ読み込んだ場合、1文字目は ``'1'`` というstr型オブジェクトである点に注意しよう。プログラム側では数値かどうかはこの時点では区別せずに、あらゆる値をstr型として扱う。文字列を数値として利用したい場合には後述する **キャスト(cast)** により変換する必要がある。
```

````{tip}
- ファイル読み込みには [{index}`readline関数`, {index}`readlines関数`](https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readline) が用意されている。
  - ``readline(size=-1)``
    - 引数sizeを省略した場合には、ストリーム（ここではファイルハンドラ）から1行読んで返す。
  - ``readlines(hint=-1)``
    - 引数hintを省略した場合には、ストリームからファイル全体を読んでリストとして返す。各行はstr型オブジェクトとして保存されている。ファイルサイズが巨大な場合にはメモリを超えてしまうため、read関数かreadline関数を使うことを検討しよう。
```Python
# readlineを使った例。
# iris.data は以下からダウンロード。
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
filename = 'iris.data'
with open(filename, 'r') as fh:
    line_no = 1
    while True:
        line = fh.readline()
        if line == "":
            break
        else:
            print('{}行目の中身: {}'.format(line_no, line))
            line_no += 1
print('ファイル読み込み終了')
```
````

---
## キャストの利用
テキストファイルを読み込んでいる場合、原則として **読み込んだあらゆる値はstr型オブジェクト** として扱われる。readlinesの場合にはリストになっているが、リスト内の各要素はstr型オブジェクトである。このため、テストの採点結果のような数値データが書かれたテキストファイルであったとしても読み込んだ時点ではstr型オブジェクトとなる。文字列を数値として利用したい場合には **{index}`キャスト<きゃすと-キャスト>`({index}`cast`)** により変換する必要がある。以下に示すコード例は文字列を int, float にキャストしている例だ。

```python
>>> data = '123'
>>> type(data)
<class 'str'>
>>> value = int(data)
>>> type(value)
<class 'int'>
>>> value
123
>>> value2 = float(data)
>>> type(value2)
<class 'float'>
>>> value2
123.0
```

ファイル読み込みの際には不要だが、数値をstr型に変換したい場合（例えば文字列結合）には数値を予めstr型にキャストする必要がある。これは上記同様に[str](https://docs.python.org/ja/3.8/library/stdtypes.html#str)関数を用いてキャストすることになる。

````{warning}
ここで見てきたように int, float, str に限らず、list, tuple, dict 等の型として提供されている標準オブジェクトの名称は、関数としても提供されている。これらの型名を変数名として利用するのは絶対に避けよう。

```python
>>> data = '123'
>>> int = 10
>>> int(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```
上記3行目ではint関数によりキャストするつもりだったが、その前の2行目で **intを変数として設定している**。このためint関数が上書き（削除）され、ただのintという名前の変数になってしまった。これは極端な例だが、リストを保存するための変数として変数listを用いるコードを書いてしまうことはとても多い。これは絶対に避けよう。
````

---
## 代表的な読み書きのための関数
- [io --- ストリームを扱うコアツール](https://docs.python.org/ja/3/library/io.html)
  - 中でも、 read(), readline(), readlines(), write(), writelines(), flush() あたりは使う可能性高いかも。

`````{admonition} 検討
次の書式でテストの採点結果が保存されてたテキストファイルを作成し、保存しよう。ファイル名をtarget.txtとする。このファイルを読み込み、テスト受験者のアカウント(str型)と採点結果(int型)として扱うコードを検討せよ。

```
e215789,100
e215780,60
e215778,80
```

````{dropdown} 回答例
```python
filename = 'target.txt'
with open(filename, 'r') as fh:
    for line in fh.readlines():
        items = line.split(',')
        if len(items) == 2:
            account = items[0]
            score = int(items[1])
            print(type(account), account)
            print(type(score), score)
        else:
            print('エラー：ファイル内の記述形式がおかしい')
            break
```
````
`````

```{note}
上記のように「特定の区切り文字で値が列挙される形で整理されたテキストファイル」のことを **{index}`CSVファイル`({index}`character separated values file`)** と呼ぶ。区切り文字としてはカンマやタブが用いられることが多く、そのようなファイルを読み込むためのツールも用意されていることが多い。ここではファイル読み込みの練習ということで自前で実装してみた例を示した。
```

---
## 参考サイト等
- 教科書4.6節。図4.12。
- [7.2. Reading and Writing Files / Python Tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Dive Into Python 3, 第11章 ファイル](http://diveintopython3-ja.rdy.jp/files.html)
- [Python3: open()](https://docs.python.org/3/library/functions.html#open)
- [io --- ストリームを扱うコアツール](https://docs.python.org/ja/3/library/io.html)

---
## 復習・予習
- 復習
  - 適宜過去資料及び教科書を参照しよう。
- 予習
  - 4.2 Specifications
  - 4.1 Functions and Scoping
