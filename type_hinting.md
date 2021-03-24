# 型ヒント

## 背景
標準関数や第三者が提供しているモジュールの多くはAPIドキュメントが用意されており、それを読めば使い方が分かる。これに対し自作した関数にはAPIドキュメントがなく、第三者はコードを読まないと分からないし、場合によっては読んでも良く分からないかもしれない。第三者に対し設計意図や使い方等を伝えやすくするための工夫が **型ヒント(type hints, type hinting)**, **docstringドキュメント**, **doctestによるテスト** だ。

---
## 型ヒント
あなたは[str.split](https://docs.python.org/ja/3.8/library/stdtypes.html#str.split)のAPI ``str.split(sep=None, maxsplit=-1)`` だけを見て、第1引数sepに何を設定するのか、戻り値が何なのかがすぐに分かるだろうか。その後の解説文や使用例まで眺めると想像できるが、def文からも補足したい。このような場合に使うのが **型ヒント(type hinting)** だ。

---
## 型ヒントの例
2つのコード例を比べてみよう。違いはdef文のみである。

```python
# これまでの型ヒントなし記法
def evaluation(score):
    if score >= 90:
        eval = 'A'
    else:
        eval = 'F'
    return eval

# 型ヒントあり
def evaluation(score: int) -> str:
    if score >= 90:
        eval = 'A'
    else:
        eval = 'F'
    return eval
```

前者の従来記法でも、第1引数scoreを利用することは分かるが、それ以上のことは関数実装を眺めないと分からない。これに対し後者の例では第1引数がint型であり、戻り値がstr型であることが1行目だけで分かる。このように関数定義における引数・戻り値の型に関するヒントを記述するのが型ヒントである。

---
## 型ヒントの書き方
型ヒントを書くには ``def function_name(arg1: type1, arg2: type2,,,) -> typeN:`` という書式で書くことになる。通常よりも1行に書く分量が増えるため横長になりやすい。これを避けるために以下のように「変数列挙の途中で改行」を入れても構わない。改行を挟む際にはインデントで引数を揃えてやると読みやすくなる。

```python
# 引数列挙時に改行を挿入した例
def calc_triangle_area(height: int,
                        width: int) -> float:
    return height * width / 2

print(calc_triangle_area(1, 2))
```

ところで上記コードでは引数にint型を指定しているが、三角形の面積を求める際の引数としてはfloat型でも問題ないし、実際に今回のコードではint型に限定する特段の理由はない。このような「int型もしくはfloat型」のように複数いずれかの型を指定して構わないことをヒントとして書く際には次のように書こう。

```python
# Unionにより複数の型を許容する例
from typing import Union
def calc_triangle_area(height: Union[int, float],
                        width: Union[int, float]) -> float:
    return height * width / 2
```

上記の ``from typing import Union`` は[標準モジュール typing の Union 型](https://docs.python.org/ja/3.8/library/typing.html#typing.Union)を読み込んでいる。これを用いて型ヒントは ``Union[int, float]`` と記述しており、これでint型もしくはfloat型であることを示している。Union型は ``Union[X, Y, Z]`` のように記述することで「X, Y, Zのいずれか」のように「または」や「いずれか」を表すために用いられる。

```{note}
型ヒントは文字通りヒントに過ぎない。ヒントと異なる型を与えた場合でも実行できてしまう点に注意しよう。（確認してみよう）
```

```{tip}
リスト型や辞書型を使うには [typing.List](https://docs.python.org/ja/3.8/library/typing.html#typing.List), [typing.Dict](https://docs.python.org/ja/3.8/library/typing.html#typing.Dict) を参考にしてみよう。
```
