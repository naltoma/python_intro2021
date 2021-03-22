# 代表的な非シーケンス集合（set, dict）

## 達成目標
- 集合setで積集合・和集合を求めることができる。
- 辞書dictで要素を参照・追加・更新・検索することができる。

```{note}
list, tuple, dict等と同様だが、すべての操作を覚えておく必要はない。必要なときに調べて使えるようになろう。
```

---
## 集合
重複しない要素（同じ値ではない要素、ユニークな要素）の集合は **集合型オブジェクト(set)** として用意されている。setは ``{}`` で記述する（valueだけを列挙する）。[set](https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset)は重複除去、和集合、差集合等の集合演算が可能だ。

````{warning}
一般的な集合においては「10円玉が5枚、100円玉が1枚」ある状況を順序無しで6枚のコインがある集合として考えるだろう。しかし set においては **同じ要素は除去** して扱う。あくまでも「同じ値ではない要素、ユニークな要素」だけを扱う点に注意しよう。以下の例で確認しよう。
```python
# 重複データのあるリスト。
>>> data = [1, 2, 3, 1]
>>> data
[1, 2, 3, 1]

# 重複データを集合で用意してみる。
>>> data = {1, 2, 3, 1}
>>> data
{1, 2, 3}
```
````

---
### 集合操作
```python
# 空の集合を用意。
# {}では辞書型とみなされるため、set関数を使う。
>>> data = set()
>>> len(data)
0
>>> type(data)
<class 'set'>
>>> data
set()

# 集合に要素を追加。
>>> data.add(1)
>>> data.add(3)
>>> data.add(-1)
>>> data
{1, 3, -1}

# 集合から要素を削除。
>>> data.remove(1)
>>> data
{3, -1}

# 存在しない要素を削除しようとすると KeyError になる。
>>> data.remove(-100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: -100

# 和集合
>>> data1 = {10, 20, 30}
>>> data2 = {20, 30, 40}
>>> data3 = {30, 40, 50}
>>> data1 | data2
{20, 40, 10, 30}
>>> data1 | data2 | data3
{50, 20, 40, 10, 30}

# 積集合
>>> data1 & data2
{20, 30}
>>> data1 & data2 & data3
{30}

# 差集合
>>> data1 - data2
{10}
>>> data1 - data2 - data3
{10}
>>> data2 - data3
{20}

# 部分集合の判定
>>> small = {10, 20}
>>> small < data1
True
>>> small < data2
False
>>> small < data3
False
```

---
### 参考サイト
- [set](https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset)

---
## 辞書
### 辞書の基本操作
**辞書型オブジェクト(dictionary; dict)** も順序付けられていない集合である。[辞書型オブジェクト](https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict)では **鍵(key)と値(value)のペア** で1つの要素を管理する。例えば「プログラミング1は金曜1限目」「プログラミング演習1は金曜2限目」（講義名と開催スケジュールというペア）というように、「同種類の異なる鍵とそれに対応するな値」を列挙して利用したい場合に用いることが多いデータ型である。

コードの具体例を眺めてみよう。以下は「アカウントe215700の点数は100点」「e175799の点数は50点」「key=123のvalueは'hoge'」という3つの要素を持つ辞書型オブジェクトを用意し、要素参照・値変更・存在しないkeyの参照・新しいkeyの登録をやっている例だ。

```python
# 辞書データを用意
>>> data = {'e215700':100, 'e175799':50, 123:'hoge'}
>>> len(data)
3

# 要素参照と値の変更
>>> data
{'e215700': 100, 'e175799': 50, 123: 'hoge'}
>>> data['e215700']
100
>>> data['e215700'] = 80
>>> data['e215700']
80
>>> data
{'e215700': 80, 'e175799': 50, 123: 'hoge'}

# 存在しないkeyを参照した場合
>>> data['e175700']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'e175700'

# 存在しないkeyを参照するのではなく、=演算子で値を指定すると追加になる。
>>> data['naltoma'] = None
>>> data
{'e215700': 100, 'e175799': 50, 123: 'hoge', 'naltoma': None}
>>> len(data)
4
```

上記1行目のように、辞書型オブジェクトを用意するには ``{key1:value1, key2:value2}`` のようにkeyとvalueを ``コロン:`` で区切ることで一つの要素を記述する。

辞書の要素を参照する際にはインデックスとしてkeyを指定する。辞書型はmutableなのでvalueの値を変更できるし、最後の例のように要素自体を追加することも可能だ。

```{note}
- key指定には、int, str, tuple等の「immutableなオブジェクト」なら利用することができる。リストや、変数そのものといったmutableなオブジェクトはkeyとして指定することができない。
- keyはユニークである必要がある。（重複したkeyを異なるvalueに割り当てることはできない）
```

- list, tupleとの違い
  - list, tupleには順番があるが、**dictには順番はない**。
  - リストやタプルの場合は「参照したい要素の順番(int型オブジェクト)」をインデックスとして指定することで目的の要素を参照するが、辞書の場合は「任意のオブジェクト」で指定することで目的の要素を参照する。

```{warning}
for文のシーケンス集合指定のように「in dict」として辞書型を指定することは可能だが、**どの順番でkey,valueが参照されるかは「定義されていない」**。

- 対策例
  - 順番を指定したいなら、指定順通りに並べた（ソートした）keyシーケンス集合を用意し、そのkeyシーケンス集合を指定して反復処理する。
  - 順序付き辞書[OrderedDict](https://docs.python.org/ja/3.8/library/collections.html#collections.OrderedDict)を使う。
```

---
### dict型オブジェクトの作成方法
- dict型オブジェクトを作るには、大別して次の2通りの手続きで行う。考え方はリストと同じ。
  - (1) 辞書として作成したいオブジェクトを``key:value``の形式で用意し、そのオブジェクト群をカンマ(,)で列挙し、``{``〜``}``で囲う。
  - (2) 空の辞書``{}``を代入した変数を予め用意しておき、その変数に追加・削除する形で辞書を用意(更新)する。

- リストの作成例(1): ``key:value``の形で予め列挙する。

```python
>>> month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
>>> month_numbers['Jan']
1
>>> month_numbers[1]
'Jan'
```

- リストの作成例(2): 空の辞書を用意して、更新する。

```python
>>> month_numbers = {}
>>> len(month_numbers)
0
>>> month_numbers['Jan'] = 1
>>> len(month_numbers)
1
>>> print(month_numbers)
{'Jan': 1}
>>> print(month_numbers['Jan'])
1
>>> month_numbers[1] = 'Jan'
>>> len(month_numbers)
2
>>> print(month_numbers)
{'Jan': 1, 1: 'Jan'}
>>> print(month_numbers[1])
Jan
```

---
### dict操作（図5.10）
取り敢えずは要素参照・追加・更新・検索できるようになろう。

|dict型オブジェクトへの操作|操作の意味|
|-:|:-|
|``len(d)``|dict型オブジェクトdが持つ要素数を返す。要素数は「key:value」のペアで1件とカウント。|
|``d.keys()``|dict型オブジェクトdが持つkey一覧を返す。一覧はdict_keys型である。list()やtuple()で型変換も可能だが一度変数に保存する必要あり。|
|``len(d)``|辞書dで使われている全てのkeyをリストで返す。|
|``d.values()``|dict型オブジェクトdが持つvalue一覧を返す。一覧はdict_values型。d.keys()と同様に型変換可能。|
|``k in d``|dict型オブジェクトdの中にkというキーがある場合にTrueを返す。|
|``d[k]``|dict型オブジェクトdにおいて、キーkで参照できる値を返す。存在しない場合にはKeyErrorを返す。|
|``d.get(k, other)``|dict型オブジェクトdにおいて、キーkで参照できる値を返す。存在しない場合にはotherを返す（KeyErrorを返さない）。|
|``d[k] = value``|dict型オブジェクトdにおいて、キーkで参照できる値をvに紐付ける。既に存在する場合には置き換えられる（上書きされる）。|
|``del d[k]``|dict型オブジェクトdにおいて、キーkを削除する。（kに紐付けられていたvalueも削除される）|
|``for k in d``|dict型オブジェクトdに対して反復処理をする。|

`````{admonition} 検討
空の辞書（要素のない辞書）を用意し、以下の操作を行え。
- step 1: 要素「key='monday', value=10」を追加。
- step 2: 要素「key='tuesday', value=20」を追加。
- step 3: 要素数を確認。
- step 4: key一覧を確認。
- step 4: key='monday'の値を確認。
- step 5: key='tuesday'の値を30に変更。
- step 6: key='wednesday'を参照。(エラーになることを確認)
- step 7: in演算子で key='wednesday' を検索。

````{dropdown} 回答例
```python
>>> data = {}
>>> data['monday'] = 10
>>> data['tuesday'] = 20
>>> len(data)
2
>>> list(data)
['monday', 'tuesday']
>>> data['monday']
10
>>> data['tuesday'] = 30
>>> data['wednesday']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'wednesday'
>>> 'wednesday' in data
False
```
````
`````

---
### dictに対するfor文の例
- tupleやlistと異なり、dictは「key:value」の組で1要素を表現している。この要素をkey,valueに取って反復処理させるには次のように書こう。
  - month_numbers.itemsが何を意味するかはhelpで確認してみよう。

```python
>>> month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
>>> for key, value in month_numbers.items():
...     print('key = {0}, value= {1}'.format(key,value))
...
key = Jan, value= 1
key = Mar, value= 3
key = 2, value= Feb
key = 3, value= Mar
key = Apr, value= 4
key = 5, value= May
key = 1, value= Jan
key = 4, value= Apr
key = May, value= 5
key = Feb, value= 2
>>>
```

上記以外にも、``d.keys()``でキー一覧を用意し、それを使って反復処理参照する等、同じループ処理を書くにしても様々な書き方がある。

---
### <a name="ref">参考サイト</a>
- [公式ドキュメント: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

````{note}
リストオブジェクトの全要素に対してループ処理を実行するためには ``for item in リスト:`` のように記述する必要があった。これに対して辞書オブジェクトの全要素に対してループ処理を実行するには大別して ``dict.keys()``, ``dict.items()`` を使う2通りがある。

```python
data = {'monday': 10, 'tuesday': 30}

# case 1
# dict.keys() を使ってkey一覧を用意する。
print(data.keys())
for key in data.keys():
    print(key, data[key])

# case 2
# dict.items() を使って(key, value)のペアで一覧を用意する。
print(data.items())
for key, value in data.items():
    print(key, value)
```
````

```{tip}
keyとvalueのペアで格納するデータ構造を[ハッシュテーブル(hash table)](https://ja.wikipedia.org/wiki/ハッシュテーブル)と呼びます。リンク先の図にあるように、実際の動作としては「与えられたkeyをindex(ハッシュ値)に変換し、そのindexにvalueを格納する」ように処理します。興味のある人はハッシュ関数・ハッシュ値・ハッシュテーブルについて調べてみよう。
```

---
## 復習・予習
- 復習
  - 適宜過去資料及び教科書を参照しよう。
- 予習
  - 4.2 Specifications
  - 4.6 Files
