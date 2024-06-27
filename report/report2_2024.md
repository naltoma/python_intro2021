# 課題レポート2: 関数定義と条件分岐に慣れよう

## 課題概要
- 関数を定義し、実行できるようになろう。
    - Level 1, 2, 4 は授業3週目の内容＋ヒントでやれます。
- 条件分岐を用いて実行するコードを切り替えられるようになろう。
    - 条件分岐は授業4週目にやります。Level 3 はその後に取り組むとよいでしょう。

---
## 取り組み方
- 友人らと話し合って取り組んで構わないが、考察は自分自身の言葉で述べること。試して分かったこと、自身で解決できなかった部分等についてどう取り組んだか、といった過程がわかるように示すこと。考えを図表や文章を駆使して表現して報告する練習です。
  - ある事象について妥当と思われる表現が思い浮かばないのなら、そのことを先輩らに尋ねてみよう。

---
## Level 1: 引数なしの関数。（5分想定）
あなたはスマホアプリを作成しているとします。そのアプリを起動した際に「Welcome!」と出力させたいと考えています。ただし実際の出力はターミナル出力で構いません。

以下の指定通りに出力する関数を作成し、実行してください。ただし以下の条件を守ること。
- 条件
    - 関数名: ``init_app``
    - 引数: なし
    - 戻り値: なし
    - 出力: ``Welcome!``
- レポートに含める内容
  - 書いたコード。
  - 動作を確認できる実行結果。
    - VSCodeで実行したならば、**VSCode内のターミナル画面のコピペで良い**。以下の例は実行の様子と結果を区別しやすくするためだけに、インタプリタ上で実行しています。
- 実行例
  - **あくまでも例** であるため、出力形式が多少違ってても処理結果を確認できるなら良いものとする。
  - 必ずしもインタプリタ上で実行する必要はない。<u>今後はこの説明を省略します</u>。

```Python
>>> init_app()
Welcome!
```

---
## Level 2: 引数ありの関数。（30分想定）
単に文字列を出力するだけでは味気ないので、少し見栄えを良くしたいです。またデバイス毎に表示表行きが異なるためサイズ調整をしたいと考えています。

指定通りに出力する関数を作成し、実行してください。ただし以下の条件を守ること。
- 条件
    - 関数名: ``init_app2``
    - 引数: 1つ
        - size: 1以上の自然数。
    - 戻り値: なし
    - 出力: 実行例参照。sizeに応じて出力文の前後に ``#`` を追加する。
- レポートに含める内容
  - 書いたコード。
  - 動作を確認できる実行結果。
    - VSCodeで実行したならば、**VSCode内のターミナル画面のコピペで良い**。以下の例は実行の様子と結果を区別しやすくするためだけに、インタプリタ上で実行しています。
- 実行例
```Python
>>> init_app2(2)
## Welcome! ##
>>> init_app2(size=3) # 引数名を指定する書式の例
### Welcome! ###
```

```{hint}
- 「小さく作る」ことを意識しましょう。
    - 例えば今回だとまずは「Welcome!の前に#を付けてみる」=>「指定個数に増やしてみる」=>「後ろに#を付けてみる」=>「後ろを指定個数に増やしてみる」ぐらいにステップ分けして考えられそうです。このように「サブゴールを設計し、動作確認しながら一歩ずつ積み上げていく力」を身につけることがとても重要です。
- 文字列を指定数出力するには `*` 演算子を使いましょう。例えば `'@' * 3` を実行した結果を出力してみてください。
- 実行例では size=2, size=3 の2パターンのみを示していますが、他の自然数でも動作することを確認しましょう。
```

---
## Level 3: 条件分岐の利用。（30分想定）
初めてアプリを起動した場合と、ユーザ登録を済ましてユーザ名を把握している場合とで出力を変更したいです。

指定通りに出力する関数を作成し、実行してください。ただし以下の条件を守ること。
- 条件
    - 関数名: ``init_app3``
    - 引数: 2つ
        - size: 1以上の自然数。int型。
        - name: ユーザ名。str型。ただし入力されない場合もある。
            - 入力されない場合とは、まだユーザ登録を済ましていないためユーザ名を把握していない状況を指します。この状況を、``name=''``として空の文字列が与えられた場合として考えるものとします。
            - 既にユーザ登録を済ました状況ならば、``name='ユーザ名'``としてユーザ名を直接与えるものとします。
    - 戻り値: なし
    - 出力: 実行例参照。sizeに応じて出力文の前後に ``#`` を追加する。
- レポートに含める内容
  - 書いたコード。
  - 動作を確認できる実行結果。
    - VSCodeで実行したならば、**VSCode内のターミナル画面のコピペで良い**。以下の例は実行の様子と結果を区別しやすくするためだけに、インタプリタ上で実行しています。
- 実行例
```Python
>>> init_app3(2, 'naltoma') # ユーザ登録が済んでいる例
## Welcome naltoma! ##
>>> init_app2(3, '') # ユーザ登録がまだの例
### Welcome new player! ###
```

````{hint}
ある条件に基づいて処理を変更する必要がある場合には条件分岐を使うことになります。ここでポイントとなるのが「条件式は何か」「Trueブロックとして処理したい内容は何か」「Falseブロックとして処理したい内容は何か」です。以下は条件式についてのヒントです。
- 変数に保存されているリテラルがstr型であることを前提に、その中身が ``''`` か否かで処理を書き分ける必要があります。
- ある値に等しいかどうかを判断するための演算子は ``==`` です。等しくないことを判断したい場合には ``!=`` 演算子を利用することができます。以下はこれらの演算子を用いた例です。
```Python
>>> 2 == 3
False
>>> something = 'naltoma'
>>> something == 'naltoma'
True
>>> something == 'nal'
False
```

条件分岐自体が良く分からない場合には教科書や授業資料、または[(外部サイト)フローチャートでの分岐の書き方](https://kaizen-penguin.com/flowchart-branch-how-to-6979/)を参考に復習してみましょう。
````

---
### Level 4: 戻り値の利用。（15分想定）
Level 1〜3の話とは全く無関係です。

以下の条件を満たす関数を作成し、実行してください。
- 条件
    - 関数: $f(x) = \sqrt{x}$
        - 関数名: ``f``
        - 引数: x。関数fへの入力。float型。
        - 戻り値: 関数fに入力xを与えた際の答え。
- レポートに含める内容
  - 書いたコード。
  - 動作を確認できる実行結果。
    - VSCodeで実行したならば、**VSCode内のターミナル画面のコピペで良い**。以下の例は実行の様子と結果を区別しやすくするためだけに、インタプリタ上で実行しています。
- 実行例
```Python
>>> result = f(10)
>>> print(f"{result=:.5f}")
result=3.16228
```

````{hint}
- 平方根のように、数学で良く用いられる関数は[mathモジュール](https://docs.python.org/ja/3/library/math.html)として提供されている。例えば $\sqrt{4}$ を求めるためには次のように書く。importの詳細は後日説明します。
- ``import math`` は、スクリプトファイルの冒頭1行目に一度書いておけば、それ以降（2行目以降）では事由にmathモジュール内の関数を利用することができます。
```Python
>>> import math
>>> result = math.sqrt(4)
>>> print(result)
2.0
```

- `f"{result=:.5f}"`は、f-string形式で変数resultを出力させるとともに、小数点以下5桁に丸めて出力するように指示しています。以下の実行結果を比較してみてください。以下では円周率(math.pi)をそのまま出力した場合、桁数を指示した場合を見比べています。
```Python
>>> import math
>>> print(math.pi)
3.141592653589793
>>> print(f"{math.pi=}")
math.pi=3.141592653589793
>>> print(f"{math.pi=:.3f}")
math.pi=3.142
>>> print(f"{math.pi=:.5f}")
math.pi=3.14159
```
````

```{tip}
f-string形式について興味がある人は[公式ドキュメント: 7.1.1. フォーマット済み文字列リテラル](https://docs.python.org/ja/3.8/tutorial/inputoutput.html#formatted-string-literals)を眺めてみるとよいでしょう。
```

---
### オプション1: 数値微分の実装。
時間に余裕のある人は取り組んでみてください。

微分積分学ST1を受講しているあなたは導関数を求めることが面倒に感じました。ひょんなことから[数値微分(numerical differentiation)](https://en.wikipedia.org/wiki/Numerical_differentiation)を使えば任意の関数について微分を求めることができると知りました。

数値微分に基づき微分を求める関数を作成し、実行してください。ただし以下の条件を守ること。
- 条件
    - 関数: 数値微分を求める関数。
        - 関数名: ``numerical_differentiation``
        - 引数: 3つ
            - function: 微分を求めたい関数名。（変数だけではなく、関数自体を引数として与えることもできます）
            - x: 微分を求めたいfloat型。
            - h: 微小な値。
    - 数値微分の求め方。
        - 中心差分近似を使いましょう。具体的には以下の式を用いて求めます。式を見て分かる通り、元の関数f(x)に微小な値hを加算した値、減算した値を与えた際の答えに基づき微分を求めることが出決まるため、数値微分では導関数を必要としません。ただしこれはあくまでも近似解です。関数の特性やhの値に応じて誤差が大きくなることがありますので注意しましょう。
        - 参考: (外部サイト) 数値微分: [ [前編](https://gihyo.jp/dev/serial/01/java-calculation/0069?summary) | [中編](https://gihyo.jp/dev/serial/01/java-calculation/0070?summary) | [差分法](https://gihyo.jp/dev/serial/01/java-calculation/0071?summary) ]

$$
f'(x) = \frac{f(x+h) - f(x-h)}{2h}
$$

- レポートに含める内容
  - 書いたコード。
  - 動作を確認できる実行結果。
    - VSCodeで実行したならば、**VSCode内のターミナル画面のコピペで良い**。以下の例は実行の様子と結果を区別しやすくするためだけに、インタプリタ上で実行しています。
- 実行例
```Python
>>> result = numerical_derivative(f, 4, 0.1)
>>> print(f"{result=:.5f}")
result=0.25002
```

---
### オプション2: 数値微分の考察。
Level4では $f(x) = \sqrt{x}$ を実装し、オプション1では数値微分を求める関数 numerical_derivative を実装した。しかし numerical_derivative(f, 4, 0.1) の結果は 0.25002 であった。これはあなたの知っている答え（$\sqrt{4} = 2$）とは異なるはずだ。

このことについてオプション1で示した参考サイトや文献、他Webページ等を調査し、何故ここまで異なる値が出るのか、どうやればより近い値を得ることができるかについて調査し、その結果を報告せよ。