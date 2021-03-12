# 演習4: マニュアル（ヘルプor公式ドキュメント）の利用

## help()コマンド・公式ドキュメントの利用
- 作業内容
  - print()関数について、help()コマンドか公式ドキュメントで調べよ。
- 補足
  - レポートには、print()関数について説明している箇所冒頭数行程度を掲載し、分かったこと、分からないことについて言及せよ。

`````{admonition} 補足
````{dropdown} 回答例
```python
help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
```
引数sepやendについて他の値を設定して実行してみよう。
````
`````

---
## ドキュメントの活用
- 作業内容
  - ``print('hoge', 'fuga', 'piga')`` を実行すると、それぞれの要素が「スペースで連結された文字列」として出力されるはずだ。ことのことについて、help()コマンドもしくは公式ドキュメントではどのように説明しているだろうか。該当箇所を探し出せ。
- 補足
  - レポートには、説明している箇所をコピペすること。

`````{admonition} 補足
````{dropdown} 回答例
```
sep:   string inserted between values, default a space.
```
````
`````

---
## ドキュメントを踏まえたコード作成
- 作業内容
  - 先程は「スペースで連結された文字列」として出力されたが、ここでは連結文字なしに3つの要素を繋げて出力したい。すなわち「hogefugapiga」と出力させたい。print関数で連結文字を指定する（スペースなしに連結させる）にはどうしたら良いだろうか。help()でその手段を探し出し、実現するコードを検討し、動作確認せよ。
  - 実現したコードを「ex4_3.py」というファイル名で保存し、シェル上で実行せよ。
- 補足
  - レポートには、シェル上で実行する様子と、実行結果を掲載すること。（演習4.2までと同じインタプリタ上ではないことに注意）

`````{admonition} 補足
````{dropdown} 回答例
```python
print('hoge','fuga','piga',sep='')
```
````
`````

---
## 余裕があるグループ向けのおまけ
## 演習 X: 関数を使ってみよう
### 演習 X.1: 下記コードをインタプリタに入力し、実行してみよう
```
def encount_enemy(name):
    print(name, 'に遭遇した。')
    print(name, 'はレポート課題の始まりを高らかに宣言した。')
    print(name, 'は楽しそうに待ち構えている。')

encount_enemy(name='naltoma')
encount_enemy(name='TA')
encount_enemy('naltoma')
```
- 補足
  - このコードは「3回print()実行するコードに、encount_enemy() という名前を付けて定義した（この時点ではまだ何も実行されない）。その名前を指定することでコードを実行させた。」という例である。
  - print()関数の前の空白は「半角スペース4つ」で統一しよう。
  - 何もない「空行」は必要です。改行するだけで良いですが、必ず空行を入力してください。

---
### 演習 X.2: 関数の仕組みをなんとなく理解できたら、自分で関数を書いてみよう
