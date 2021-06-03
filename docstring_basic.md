# docstringドキュメント
コード中に ``#`` から始まるコメントを書くことでもコードに対する補足を伝えることができるが、これはどちらかというと「APIドキュメントとしては蛇足だが、コード上の補足を伝える」目的で使うことが多い。これに対してAPIドキュメントのように関数の仕様や使用方法を記述するのが **docstringによるドキュメンテーション** だ。

- コメント
  - コードに対する補足。
  - 書き方
    - 1行コメントなら ``#`` で記述。
    - 複数行コメントなら ``'''〜'''`` で記述。（ダブルクォートも可）
- ドキュメント
  - 補足する文という点ではコメントと一緒。「マニュアル」としての側面が強い。
  - 書き方
    - 複数行コメントを「**特定の場所**」に書く。
      - 対象の冒頭に記述。
      - ファイル全体についてのドキュメントなら、ファイル冒頭。
      - 関数についてのドキュメントなら、関数冒頭。
    - 書き方の例
      - [Example Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
      - [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

---
## ドキュメントの参照方法
- 方法1：pydocコマンドで参照。
  - pydocコマンドはPythonの命令文 **ではない**。コマンドである。ターミナル上から使おう。
  - ソースコードが ``test.py`` なら、ターミナル上で ``pydoc test`` として参照。拡張子 .py を付けずに指定する点に注意。この拡張子を取り除いた名前を **モジュール名** と呼ぶ。
    - 以前利用した random モジュールや、random.randint 関数についても pydoc コマンドでドキュメントを参照できる。試してみよう。
  - pydoc を終了するには ``q`` を入力しよう。quit（終了）の頭文字。
- 方法2：HTML形式でドキュメントを生成し、ブラウザで参照。
  - pydocコマンド実行時に、-wオプション付きで実行。エラーが無ければ「モジュール名.html」が生成される。
  - 生成されたHTMLファイルを open コマンドで開くか、Finderからダブルクリックで開くと参照できる。

```{note}
ドキュメント参照する際にはモジュール名を指定する点に注意しよう。
```

---
## ドキュメントを書いてみよう
- コード例

```Python
def evaluation(score):
    if score >= 90:
        eval = 'A'
    else:
        eval = 'F'
    return eval

scores = [100, 20, 30]
for score in scores:
    label = evaluation(score)
    print("{} => {}".format(score,label))
```

- 手順1：コードの準備。
  - 上記コードを eval.py として保存。
- 手順2：ドキュメント生成＆参照。（docstring書く前の状態を確認）
  - ``pydoc -w averaging``
  - ``open averaging.html``
- 手順3: 文字コードを記載。
  - 1行目に ``# -*- coding: utf-8 -*-`` と書く。
  - macOS標準のドキュメント生成コマンド pydoc が古いための対応。Python3用のpydoc3ならこの記載は不要。
- 手順4-1：ドキュメント記述1（ファイル全体）
  - ファイル冒頭（2行目以下）に下記を記述。
  - 保存したらドキュメント生成し、どのように反映されるか確認してみよう。

```Python
'''ドキュメンテーションテスト。
ここにはプログラムファイル全体のドキュメントを書く。
'''
```

- 手順4-2：ドキュメント生成2（関数evaluation）
  - 関数evaluationのdefブロックに下記を記述。インデントを関数ブロックに揃えること。
  - 保存したらドキュメント生成し、どのように反映されるか確認してみよう。

```Python
def evaluation(score):
    '''点数をA〜F評価に変換するプログラム。

    Arguments:
      score (int): 点数。0〜100を想定。

    Returns:
      eval (str): 評価結果。A, B, C, D, Fのいずれか。
    '''
    if score >= 90:
        eval = 'A'
    else:
        eval = 'F'
    return eval
```

---
## 参考：ドキュメント付きソースコードと生成したドキュメントの例
- 今回の例: [ <a href="./samples/eval.py" target="_blank">eval.py</a> | <a href="./samples/eval.html" target="_blank">eval.html</a> ]
- [docstringのstyle3種の例](https://qiita.com/yokoc1322/items/ebf25c9cb779ff5ebc9c)
  - docstringの書き方に代表的なスタイルがいくつかある。上記リンク先では reStructuredTextスタイル、Googleスタイル、Numpyスタイルが紹介されている。本授業では（當間が）比較的読みやすいと感じるGoogleスタイルでの記述例を取り上げた。

````{warning}
**docstring形式で書いているつもりでも実際にはドキュメントとして扱われない** ことがある。例えば以下のコードをpydocでドキュメント生成して確認してみよう。

```python
def multiply(value1, value2):
    result = value1 * value2
    '''multiplyは2つの引数を積を求めます
    Argments:
      value1 (int, float): 数値。
      value2 (int, float): 数値。
    Returns:
      result (int, float): 積
    '''
    return result
```

上記がドキュメントとして扱われていない理由は「記述場所が誤っている」ことにある。関数に関するドキュメントならばかならずdef文の次の行から書き始めよう。コード中にdocstringを書いたとしても、それはドキュメントとしては扱われない。
````

```{note}
上記に限らず **やったことが想定通りに動作しているかどうかを確認する** ようにしよう。手軽に確認できるのがプログラミングの大きなメリットだ。
```
