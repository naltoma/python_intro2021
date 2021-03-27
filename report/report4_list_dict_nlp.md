# 課題レポート4: 基本的な自然言語処理を実装してみよう（その1）。

## 課題概要
- 文章を数値ベクトルとして表現してみよう。
- 文字列・リスト・辞書の代表的な処理に慣れよう。
- （数値ベクトル同士の類似度により文章の類似度を計測してみよう。）

---
## 取り組み方
- 友人らと話し合って取り組んで構わないが、考察は自分自身の言葉で述べること。試して分かったこと、自身で解決できなかった部分等についてどう取り組んだか、といった過程がわかるように示すこと。考えを図表や文章を駆使して表現して報告する練習です。
  - ある事象について妥当と思われる表現が思い浮かばないのなら、そのことを先輩らに尋ねてみよう。

---
## レベル1「ユニークな単語一覧を作成し、出現回数を数えよ」
- 背景
  - 文書をベクトル空間における1点として表現することができれば、ベクトル空間における距離が近ければ似ている文書であり、遠ければ似ていない文書として判断できるようになる。ここではベクトル空間モデル（ベクトル空間への写像方法）の一つとして[単語文書行列](https://ja.wikipedia.org/wiki/ベクトル空間モデル)を作りたい。
  - 単語文書行列とは、文書$d_i$に単語$t_j$が$n$回出現するとき、行列の要素$w^i_j=n$により定義される行列である。この行列を作るため、まずはユニークな単語一覧を作成し、その出現回数を数えたい。
- 課題
  - 文書はstr型で実行例のように用意するとする。文書を引数として受け取り、単語ごとの出現回数を数えあげる関数を実装せよ。関数名を ``count_unique_words`` とする。
- 補足
  - str.lower
    - 文書は英文である。大文字小文字は同一視するものとする。例えば ``Apple`` と ``apple`` は同一としよう。そのためにはすべての文字を大文字もしくは小文字に変換してしまえば区別する必要がなくなる。例えば小文字に変換するなら[str.lower](https://docs.python.org/ja/3.8/library/stdtypes.html#str.lower)を使おう。
  - str.split
    - 英語で書かれた文書は、人間が読めば「半角スペースで単語が区切られている」ことは分かる。しかしコンピュータはそのようなことは知らないため、何らかの方法で単語を切り出す必要がある。このような場合には[str.split](https://docs.python.org/ja/3.8/library/stdtypes.html#str.split)で区切り文字を指定して分割しよう。
  - レポート
    - 動作を確認できる実行結果を掲載すること。
- 実行例
```python
>>> doc1 = "I have a pen"
>>> result1 = count_unique_words(doc1)
>>> print(type(result1))
<class 'dict'>
>>> print(result1)
{'i': 1, 'have': 1, 'a': 1, 'pen': 1}
```

```{note}
> 小さく生んで大きく育てる
>
> 最初から大きな成果でなくてよい。何度もバージョンアップすればよいのだから。
> 小さくてよいので具体的なアウトプットを生み出し、それを徐々に大きな成果に育てていく。
> - 自分がやりたいことを思い描き、まずは最小限の規模で、具体的なアウトプットを生み出す。大きな構想がある場合には、その構想の縮小版や一側面を体現したものでよい。そのアウトプットを、現段階の成果として発表する。
> - そのアウトプットを修正したり、新たに追加したりすることで、徐々に成長させていく。
>
> by [ラーニング・パターン No.24, 小さく生んで大きく育てる](https://learningpatterns.sfc.keio.ac.jp/No24.html)
```

---
## レベル2「単語一覧を作成せよ」
- 背景
  - レベル1で作成した関数は、1つの文字列に対して出現回数を数えた辞書を返すことができる。これに対し、単語文書行列においては全単語に対する出現回数を数える必要がある（出現しなかった単語は0とする必要がある）。このことに対応するため以下の手順で処理したい。
    - step 1: count_unique_words を用いて複数文書に対する処理結果をリストとして保存する。
    - step 2: リスト内の全要素（全辞書）を対象に、ユニークな単語を収集した単語一覧を作成する。
- 課題
  - 文書集合はリスト型で実行例のように用意するとする。文書集合を引数として受け取り、単語一覧を作成する関数を実装せよ。関数名を ``make_word_list`` とする。
- レポート
  - 動作を確認できる実行結果を掲載すること。
  - **どのような過程を経てコードに翻訳したのか説明** すること。図等を用いても良い。
  - ソースコードは report4.py という名前で保存し、**アップロードすること**。
- 実行例
```python
>>> # 2文書を用意
>>> docs = ['I have a pen', 'I have an apple']

>>> # 単語一覧を作成、ついでにレベル1の結果も返す
>>> word_list, sentence_words = make_word_list(docs)
>>> print(type(word_list))
<class 'set'>
>>> print(word_list)
{'a', 'apple', 'i', 'have', 'pen', 'an'}
>>> print(type(sentence_words))
<class 'list'>
>>> print(sentence_words)
[{'i': 1, 'have': 1, 'a': 1, 'pen': 1}, {'i': 1, 'have': 1, 'an': 1, 'apple': 1}]
```

---
## オプション
レベル2の時点ではまだ単語文書行列を作成できていない。どのようにしたら良いだろうか。（レポート5に続く予定）