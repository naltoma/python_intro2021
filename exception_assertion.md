# 例外とアサーション
- 教科書7章。

---
## 概要
- exceptionsやassertionsを効果的に使うことで、開発者・利用者に対する情報提供や、defensive programmingを実現できる。
- **{index}`exceptions`**: {index}`例外<れいがい-例外>`
  - 一般的には「通常起きない何か」を例外と呼ぶ。プログラムではどこでも起こりうる。
  - Pythonの標準ライブラリ（四則演算, 代入, 比較, if文, for文,,,等あらゆる標準機能）においても利用されている。
    - 良く見る例外: IndentationError, IndexError, TypeError, NameError, ValueError, ZeroDivisionError
      - Tips: エラーは開発者に対する情報提供。エラーが出たらどういう意味か読み取ろう。
      - エラーは例外の一種。エラーだけが例外ではない。
      - [組み込み例外](https://docs.python.org/ja/3/library/exceptions.html) by 公式ドキュメント
- **{index}`assertions`**: 表明、断言、アサート、{index}`アサーション<あさーしょん-アサーション>`
  - 関数や手続きが「前提として想定していること」を明示するために用いる。簡易的なテストと捉えても良い。
- 関連: **{index}`warnings`（警告)**
  - [警告の制御](https://docs.python.org/ja/3/library/warnings.html) by 公式ドキュメント
    - 「警告メッセージは一般に、ユーザに警告しておいた方がよいような状況下にプログラムが置かれているが、その状況は (通常は) 例外を送出したりそのプログラムを終了させるほどの正当な理由がないといった状況で発されます。例えば、プログラムが古いモジュールを使っている場合には警告を発したくなるかもしれません。」

---
## 例外
### 例外発生の例
```python
# 例1: IndexError
>>> test = [1, 2, 3]
>>> test[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

- UNIX用語: 標準入力・標準出力・標準エラー出力
  - UNIXにおける標準で用意されているテキスト・ストリーム。
  - {index}`stdin`: 標準入力。ここではターミナル上で操作された入力のこと。
  - {index}`stdout`: 標準出力。ターミナル上への出力。print()のデフォルト出力先。
  - {index}`stderr`: 標準エラー出力。デフォルトではターミナル上への出力。
  - 参考
    - [UNIXの標準入出力とリダイレクション](http://www.rsch.tuis.ac.jp/~ohmi/literacy/stdio.html)
- **{index}`IndexError`: list index out of range**
  - Exeptionの一種。list型オブジェクトに対して、範囲外(out of range)のインデックスにアクセスしようとしたために起きた(raise)。
  - （という情報を開発者に提供するために例外という機能が利用されている）
- 例外が起きたら、
  - 通常、例外が発生するとコードの実行をそこで停止する。
  - 想定内の例外であれば、その例外に応じたコードを選択させ、実行を続けさせることもできる。

---
### 例外を扱おう
- 次のコード「例2-1」では、
  - num_failuresが0の時、ZeroDivisionErrorになる（例外が発生する）。
  - 例外が発生すると、発生した箇所でプログラムの実行が停止する。（print文2つは実行されない）

```python
# 例2-1: num_failuresが0の時、ZeroDivisionErrorになる。
def calc_ratio(num_success, num_failures):
    success_failure_ratio = num_success / float(num_failures)
    print('success_failure_ratio = {0}'.format(success_failure_ratio))
    print('Now here')

calc_ratio(5, 1)
# -> success_failure_ratio = 5.0
# -> Now here

calc_ratio(5, 0)
# -> ZeroDivisionError: float division by zero
```

- 次のコード「例2-2」は、ZeroDivisionErrorが発生してもしなくても、確実に最後のprint文を実行するコード例。
  - まず「tryブロック」のコードを実行しようとする。
  - 実行中に何も例外が発生しなければtryブロックを抜ける。exceptブロックは無視する。**最後にprint文が実行される（プログラム実行が続行する）**。
  - もし、tryブロック実行中に「ZeroDivisionError」が発生したら、それ以降のtryブロックのコードを無視してexceptブロックに移動する。exceptブロックに移動したら、指定されたコードを実行し、exceptブロックを抜ける。**最後にprint文が実行される（プログラム実行が続行する）**。

```python
# 例2-2: num_failuresが0の時、異なるコードを実行させる。
def calc_ratio2(num_success, num_failures):
    try:
        success_failure_ratio = num_success / float(num_failures)
        print('success_failure_ratio = {0}'.format(success_failure_ratio))
    except ZeroDivisionError:
        print('失敗回数0のため、success/failuer比は定義できません。')
    print('Now here')

calc_ratio2(5, 1)
# -> success_failure_ratio = 5.0
# -> Now here

calc_ratio2(5, 0)
# -> 失敗回数0のため、success/failuer比は定義できません。
# -> Now here
```

````{note}
- tryブロックを記述したら、対応するexceptブロックを最低1つ記述する必要がある。
- exceptブロックを指定する際の「例外」は、省略すると「どんな例外が起きた場合でも実行されるブロック」になる。
- 例外を複数列挙する際にはtupleを使う。（下記コード例参照）
```python
# exceptブロックの記述例
try:
    #tryブロック
except (ValueError, TypeError):
    #tryブロック処理中に、
    #ValueErrorかTypeErrorが起きた場合に処理されるexceptブロック。
except:
    #tryブロック処理中に、
    #上記以外の例外が起きた場合に処理されるブロック。
```
````

---
### polymorphicなコード
- Polymorphism <-> Monomorphism
  - {index}`Polymorphism`: {index}`ポリモーフィズム<ぽりもーふぃずむ-ポリモーフィズム>`、多態性、多相性、多様性。
    - 詳細は後記の授業プログラミング2でやります。今回は紹介のみ。
  - Monomorphism: モノモーフィズム、単態性、単相性。
- 次のコード「例3-1」は、古典的な関数や手続き（単態性なコード）の例。

```python
# 例3-1: 古典的な関数や手続き（単態性なコード）
def read_int():
    while True:
      val = input('Enter an integer: ')
      try:
          val = int(val)
          return val
      except ValueError:
          print('{0} is not an integer'.format(val))

data = read_int()
# -> Enter an integer: 123
print(data)
# -> 123

data = read_int()
# -> Enter an integer: hoge
# -> hoge is not an integer
# -> Enter an integer:
```

- 次のコード「例3-2」は、オブジェクトの型に依存しない抽象度の高い関数や手続き（多態性なコード）の例。
  - 関数が[第一級オブジェクト](https://ie.u-ryukyu.ac.jp/~tnal/2016/prog1/Higher_order_programming.html)であることも利用することで、抽象度の高い関数や手続きを記述できる。
  - ここでの「抽象度が高い」とは、オブジェクトの型毎に個別に関数を用意する（read_int(), read_float(),,,）のではなく、read_val()1つで「入力を読み込む」関数になっていることを意味している。

```python
# 例3-2: 抽象度の高い関数や手続き（多態性なコード）
def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg + ' ')
        try:
            val = val_type(val)
            return val
        except ValueError:
            print('{0} {1}'.format(val, error_msg))

data = read_val(int, '整数を入力下さい:', 'は整数ではありません!')
# -> 整数を入力下さい: 123
print(data)
# -> 123

data = read_val(float, '浮動小数点数を入力下さい:', 'は浮動小数点数ではありません!')
# -> 浮動小数点数を入力下さい: hoge
# -> hoge は浮動小数点数ではありません!
# -> 浮動小数点数を入力下さい: 1.234
print(data)
# -> 1.234
```

---
### フロー制御として利用される例外
例外は日常的に利用されている。例えば、関数実行時に何か問題が発生した際、どのような問題が発生したのかを伝えるために戻り値を利用することが多い。

Pythonでは **{index}`raise文`** を用いることで例外を強制的に発生させることができる。その関数や手続きの開発者・利用者に対する助言を提示するために使われることが多い。

```{tip}
- ``nan (Not a Number)``: [{index}`math.nan`](https://docs.python.org/3/library/math.html?highlight=nan#math.nan)
  - 数値演算結果が定義できない場合（0除算等）でも、int型もしくはfloat型を返したい（値はともかく、型を揃えたい）場合に用いることが多い。
```

```python
# 例4-1（教科書の図7.1）: raiseによるエラー文生成。
def get_ratios(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
    Returns: a list containing the meaningful values of vect1[i]/vect2[i]
    """
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios() called with bad arguments.')
    return ratios

print(get_ratios([1.0, 2.0, 7.0], [1.0, 2.0, 0.0]))
# -> [1.0, 1.0, nan]

print(get_ratios([], []))
# -> []

print(get_ratios([1.0, 2.0], [3.0]))
# Traceback (most recent call last):
#   File "<stdin>", line 8, in get_ratios
# IndexError: list index out of range
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 12, in get_ratios
# ValueError: get_ratios() called with bad arguments.
```

---
### 検討課題：例外処理を書いてみよう。
`````{admonition} 検討課題：例外処理を書いてみよう。
あなたは、用意したテキストファイルを読み込み何か処理するプログラム（下記）を書いている最中だとします。
```Python
# コード書きかけ
filename = "naltoma.txt"
with open(filename, "r") as f:
    for line in f.readlines():
        print(line)
```
- やること
  - (1) 上記コードは naltoma.txt を読み込む想定で書きました。意図的にこのテキストファイルが存在しない状態で上記コードを実行し、例外として ``FileNotFoundError``が起こることを確認してください。
  - (2) FileNotFoundError時にプログラムの実行が強制終了するのではなく、例外処理を行い、ファイルが存在しない場合には「naltoma.txtが見つかりません。ファイルを用意してから実行してください。」と出力してから通常終了するようにコードを修正してください。また例外処理が正しく動作する（メッセージ出力して通常終了する）ことを確認してください。
  - (3) naltoma.txt を用意し、意図的にファイルへの読み込み許可を取り消してください。naltoma.txtの中身は自由で構いません。読み込み許可を取り消すには、例えば ``chmod u-r naltoma.txt`` によりuserからread権限を取り消すことができます。権限を取り消す前と取り消した後とで権限（パーミッション）が変わっていることを、``ls -l`` で確認してください。
  - (4) 読み込み許可がない状態で改めてプログラムを実行し、例外として ``PermissionError`` が起こることを確認してください。
  - (5) PermissionError時にプログラムの実行が強制終了するのではなく、例外処理を行い、パーミッションが不適切な場合には「パーミッションを確認し、適切な権限を付与してから実行してください。」と出力してから通常終了するようにコードを修正してください。また例外処理が正しく動作する（メッセージ出力して通常終了する）ことを確認してください。

````{dropdown} (2)の解答例
```Python
# (2)の解答例
filename = "naltoma.txt"

try:
    with open(filename, "r") as f:
        for line in f.readlines():
            print(line)
except FileNotFoundError:
    print(f"{filename=}が見つかりません。ファイルを用意してから改めて実行してください。")
```
````

````{dropdown} (3)の確認例
```shell
(base) oct2021:tnal% ls -l naltoma.txt
-rw-r--r--  1 tnal  staff  0  6 30 14:36 naltoma.txt
(base) oct2021:tnal% chmod u-r naltoma.txt
(base) oct2021:tnal% ls -l naltoma.txt
--w-r--r--  1 tnal  staff  0  6 30 14:36 naltoma.txt
```
````


````{dropdown} (5)の解答例
```Python
# (5)の解答例
filename = "naltoma.txt"

try:
    with open(filename, "r") as f:
        for line in f.readlines():
            print(line)
except FileNotFoundError:
    print(f"{filename=}が見つかりません。ファイルを用意してから改めて実行してください。")
except PermissionError:
    print(f"{filename=}を読み込むことができませんでした。パーミッションを確認し、適切な権限を付与してから実行してください。")
```
````

`````

---
## アサーション
- {index}`Assertions` ({index}`アサーション<あさーしょん-アサーション>`)
  - 強いて訳すなら「表明、断定」だが、通常は日本語でもアサーションとカタカナ表記されることが多い。
  - 関数や手続きが「前提として想定していること」を明示するために用いる。簡易的なテストと捉えても良い。引数が想定通りであることをチェックするために用いられることが多いが、これはuseful defensive programming toolの例。
  - もしアサーションに遭遇したら、指定された条件を満足しているか評価され、満足している(True)ならそれ以降の処理に進む。満足していない(False)なら、**{index}`AssertionError`**が生じ、プログラム実行を停止する。
- assert文の書式
  - ``assert 評価式``
  - ``assert 評価式, 引数``: 引数にエラー文を指定しておくと、raiseと同じ使い方ができる。

```python
# 例5: アサーションの例
def get_ratios2(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
    Returns: a list containing the meaningfulvalues of vect1[i]/vect2[i]
    """
    assert len(vect1) == len(vect2), "vect1とvect2の要素数は揃えて下さい!"
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios() called with bad arguments.')
    return ratios

print(get_ratios2([1.0, 2.0, 7.0], [1.0, 2.0, 0.0]))
# -> [1.0, 1.0, nan]

print(get_ratios2([], []))
# -> []

print(get_ratios2([1.0, 2.0], [3.0]))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 5, in get_ratios2
# AssertionError: vect1とvect2の要素数は揃えて下さい!
```

---
## 参考サイト
- [第一級オブジェクト](https://ie.u-ryukyu.ac.jp/~tnal/2016/prog1/Higher_order_programming.html)
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) by 公式ドキュメント
- [assert statement](https://docs.python.org/3/reference/simple_stmts.html#assert) by 公式ドキュメント
- [組み込み例外](https://docs.python.org/ja/3/library/exceptions.html) by 公式ドキュメント
- [警告の制御](https://docs.python.org/ja/3/library/warnings.html) by 公式ドキュメント
