# doctest
## 概要
> {index}`doctest モジュール`は、対話的 Python セッションのように見えるテキストを探し出し、セッションの内容を実行して、そこに書かれている通りに振舞うかを調べます。
>
> [公式ドキュメント:doctest](https://docs.python.org/ja/3/library/doctest.html)より引用。

一般的に、プログラミングにおける関数は、その関数に与える入力（引数）と関数の出力（戻り値）を最初に決めて（理解）から、実装方法を検討（整理）し、実装（翻訳）する。その実装した関数が正しく動作することを確認するには print 出力したり、debug実行したりするのも手だが、毎回目視確認するのはシステムが大規模化してくると辛くなる。例えば100個の関数があるプログラムを想像してみよう。1行だけ変更した際にすべての関数が正しく動作することを確認するために print 文追加しまくったり、デバッグ実行で確認したりしたいだろうか。

動作検証に要する手間をなるべく省力化するための技術は **{index}`Testing` ({index}`テスト<てすと-テスト>`)** と呼ばれている。テスト対象が関数の場合には **{index}`単体テスト<たんたいてすと-単体テスト>`（{index}`Unit test`）**、複数の関数を組み合わせたものが対象となる場合には **{index}`結合テスト<けつごうてすと-結合テスト>`（{index}`Integration test`）** 等、様々なテスト技法が提唱されている。

```{note}
- テストの効果。
  - 直接的には動作確認を自動化しやすくなる。
  - 間接的には、中長期的なコード開発を支援する。例えば機能追加削減等のコード修正をする場面を想像してみよう。ある関数内の1行を修正した際に、その関数だけならともかく、それ以外の部分に影響が及んでいないかどうかをどう確認したら良いだろうか。テストを自動化してくれれば、その影響範囲を掴みやすくなる。
```

今回は Python における単体テストの一つとみなせる [{index}`doctest`](https://docs.python.org/ja/3/library/doctest.html) の例を眺め、テストの書き方や実施方法を学んでいこう。

---
## コード例1（モジュールレベルのテスト）
モジュールドキュメント内にテストを書いた例を眺めてみよう。

```Python
"""
てすとだよ〜。
>>> result = 1 + 2
>>> print(result)
3
"""
```

- 上記を ``testing1.py`` として保存。
  - これはdocstringドキュメントであり、本来は「人間に向けた説明書」である。
- 動作確認1、通常実行。
  - ファイル実行したとしても実行すべき命令文がどこにもないため、何も出力されないし、エラーも出ない。
- 動作確認2、テスト実行。
  - 2通りの方法がある。
    - case 1: ``python -m doctest testing1.py``
      - case 1 では、テストが失敗した部分だけを報告（出力）する。テストが通った（想定通りであることを確認できた）部分は報告しない。
      - 今回のコードでは全てのテストが成功するため、報告は省略される。
    - case 2: ``python -m doctest testing1.py -v``
      - case 2 では、テストの成功・失敗を問わず全ての検証結果を報告する。
      - 今回のコードでは2件のテスト結果が報告される。
- テストの書き方
  - docstringドキュメントの中に書く。
  - Pythonインタプリタ上での動作をイメージして、実行例を書く。
    - 実行例、すなわち実例を書く必要がある。例えば ``print(1)`` ならば ``1`` が出力されるというように、具体的に実行する命令文とその命令文を実行した際に得られる結果を用意する必要がある。
  - 注意点
    - **インデントはdocstringドキュメントに合わせる**。
    - **テストが通るかどうかの判定は文字列判断により行われる**。
      - **スペースの有無も厳密にチェックされる**。
      - 例えば、```>>>print(1)``` は、スペースが抜けているためテストそのものが実行できません。

````{warning}
「テストが通るかどうかの判定は文字列判断により行われる」ことを確認して見るために、先程のコード例で ``print(result)`` の結果を ``3 `` としてみよう。つまり3の後ろにスペースを一つ以上加えてみよう。見かけ上は先程のコードと同じに見えるはずだが、結果が異なる（テストが失敗する）はずだ。
````

---
## コード例1のテスト結果に対する詳細確認
今回は全てのテストが通るため、``-v`` オプションを付けて詳細報告をさせよう。
- 報告1件目：Trying〜ok
  - ``Tring`` は、テスト対象コード。今回は ``result = 1 + 2`` を試した。
  - ``Expecting`` は、上記コードの実行後に期待すべき応答。今回は ``nothing`` で、戻り値は無いことを期待。
  - ``ok`` は、実際に期待通りの応答を得たという回答。
  - 補足
    - 「ある命令文を実行して、その戻り値を変数に保存する。その際に出力はなにもない。」ということを確認するのも一つのテストとして扱われる。
- 報告2件目：Trying〜ok
  - ``print(result)`` の結果として ``3`` が得られることを期待し、実際にそうだったことを確認した。
- サマリ：それ以降（全てのテスト結果に関する要約）
  - testing1モジュールの中に2件のテストがあった。
  - 2件期待通り（pass）であり、0件失敗した。

```shell
(base) oct:tnal% python -m doctest testing1.py -v
Trying:
    result = 1 + 2
Expecting nothing
ok
Trying:
    print(result)
Expecting:
    3
ok
1 items passed all tests:
   2 tests in testing1
2 tests in 1 items.
2 passed and 0 failed.
Test passed.
```

```{note}
- doctestの特徴
  - 「読めるテスト」にも「実行できるドキュメント」にもなる。
```

---
## コード例2（関数のテスト）
- 関数ドキュメント内にテストを書いた例を眺めてみよう。
- コード例
  - 下記を ``testing2.py`` として保存。
    - 関数 add を定義。
    - docstringによるドキュメントを記述。
    - ドキュメントの中に、Python インタプリタ上で実行する様子を記述。

```python
"""An example of doctest.

This module supplies one function, add(). For example,

>>> add(1, 2)
 3
"""

def add(arg1, arg2):
    """Return the added value for arg1 and arg2.

    Args:
        arg1 (int or float): a number of int- or float-object.
        arg2 (int or float): a number of int- or float-object.

    Returns:
        result (int or float): the added value arg1 and arg2

    >>> add(-1, 3)
    2
    >>> add(0, 0.5)
    0.5
    """
    result = arg1 - arg2
    return result


if __name__ == "__main__":
    print(add(1,2))
```

- 動作確認その1、通常実行。
  - ``python testing2.py``
  - 問題なければ最下部の ``print(add(1,2))`` を実行した結果として ``-1`` が出力されているはず。
  - 本来の add(1,2) の結果は 3 を出力してほしいが、意図的にバグ混入コードとしているため、現時点では結果が異なっている。
- 動作確認その2、テスト実行。
  - テストが通る部分の報告を省略させるため、case 1の方法（-vオプションなし）でテスト実行しよう。
  - 未編集の testing2.py をテスト実行すると、多数の結果とともに最後にそれらの要約である ``***Test Failed*** 3 failures.`` が報告されるはずだ。これは「テストは失敗した。3件失敗している」と報告している。

---
## コード例2のテスト結果に対する詳細確認
- 報告1件目（下記）
  - 確認事項
    - ``Failed example`` ということで、失敗事例を報告している。該当テストは5行目にあり、具体的には ``add(1, 2)`` で失敗したことを報告している。
    - ``Expected`` として記述されている 3 が戻ってくることを期待していた。
    - しかし、``Got`` として異なる値が戻ってきた、具体的には -1 が戻ってきたことを報告している。これは期待した値と異なるため、テスト失敗と判定された。

```shell
oct:tnal% python -m doctest testing2.py
**********************************************************************
File "/Users/tnal/prog1/testing2.py", line 5, in testing2
Failed example:
    add(1, 2)
Expected:
     3
Got:
    -1
```

- 報告2件目（下記）
  - 確認事項
    - 試したコードは何だろう？
    - その結果、何が得られることを期待しているだろう？
    - 実際には何が得られたのだろう？

```shell
**********************************************************************
File "/Users/tnal/prog1/testing2.py", line 20, in testing2.add
Failed example:
    add(-1, 3)
Expected:
    2
Got:
    -4
```

- 報告3件目（下記）
  - 確認事項
    - 試したコードは何だろう？
    - その結果、何が得られることを期待しているだろう？
    - 実際には何が得られたのだろう？

```shell
**********************************************************************
File "/Users/tnal/prog1/testing2.py", line 22, in testing2.add
Failed example:
    add(0, 0.5)
Expected:
    0.5
Got:
    -0.5
```

- サマリ
  - 確認事項
    - 全体で何件のテストがあったのだろう？
    - 成功したテスト件数は？
    - 失敗したテスト件数は？

```shell
**********************************************************************
2 items had failures:
   1 of   1 in testing2
   2 of   2 in testing2.add
***Test Failed*** 3 failures.
```

---
## 修正1：add関数の修正
- よく見ると、add関数の演算子を間違えて ``-`` で演算している。これを ``+`` に修正しよう。
- 編集＆保存し直したら、改めてテスト実行しよう。その結果どうなるだろうか？
- 報告結果
  - 確認事項
    - 1件失敗が報告されている。それはどこだろうか？
    - どういう失敗だろうか？

```shell
oct:tnal% python -m doctest testing2.py
**********************************************************************
File "/Users/tnal/prog1/testing2.py", line 5, in testing2
Failed example:
    add(1, 2)
Expected:
     3
Got:
    3
**********************************************************************
1 items had failures:
   1 of   1 in testing2
***Test Failed*** 1 failures.
```

---
## 修正2：テストの修正
- 修正1反映に伴う現状確認。
  - ExpectedとGot内の数値は同じだが、何やらインデントがずれているようだ。doctestを確認してみると `` 3`` として冒頭にスペースが付いているらしい。これは、**``add(1, 2)`` を実行すると、冒頭にスペースが付いた状態で3が出力されることを期待している** というテストを書いていることになる。本来はスペースは不要で、単に足した結果を戻してくれれば良いはずだ。つまり、この例は、テスト自体を書き損じた例である。
- テストの修正。
  - `` 3`` を ``3`` に修正しよう。（スペースを削除しよう）
- テスト実行。
  - 今回は全てのテストが通るはずだ。

---
## 検討

`````{admonition} 検討
3つの課題に対する採点結果を``scores = [50, 100, 80]``として用意したとしよう。以下に示す関数get_total_score()は、このリストを受け取ると合計点を返してくれる関数だ。この関数に対し動作を確認するためのdoctestを記述し、テストを実行してみてください。なおテストでは [0, 50] を入力されると 50 が返ってくることを確認してください。
```Python
def get_total_score(scores: list[int]) -> int:
    result = 0
    for score in scores:
        result += score
    return result

if __name__ == "__main__":
    #動作確認
    scores = [50, 100, 80]
    print(get_total_score(scores))
    print(get_total_score([1, 2, 3]))
```
````{dropdown} 回答例
```python
def get_total_score(scores: list[int]) -> int:
    '''
    >>> get_total_score([0, 50])
    50
    '''
    result = 0
    for score in scores:
        result += score
    return result

if __name__ == "__main__":
    #動作確認
    scores = [50, 100, 80]
    print(get_total_score(scores))
    print(get_total_score([1, 2, 3]))
```
上記を sample.py と保存したなら、
- 確認方法1: ``python -m doctest sample.py`` として何も出力されないならテストがパスしているはず。
- 確認方法2: ``python -m doctest sample.py -v`` として具体的なテスト結果が出力され、「1 passed and 0 failed.」となるはず。
````
`````

---
## 復習・予習
- 復習
  - 適宜過去資料及び教科書を参照しよう。
- 予習
  - 4.1.2 Keyword Arguments and Decault Values
  - 4.1.3 Scoping
  - 5.3 Lists and Mutability
