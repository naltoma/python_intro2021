# デバッグ実行入門

## デバッグとは
コードの誤り・欠陥等の{index}`バグ<ばぐ-バグ>`（{index}`bug`）を修正しようと試みる行為を{index}`デバッグ<でばっぐ-デバッグ>`（{index}`debug`）と呼ぶ。代表的なデバッグ方法としては (1)print出力、(2)デバッガの利用がある。

print出力では、文字通り気になるところでその都度print出力することになる。出力することで中身を確認できるが、その都度記述する必要があるため手間ががかり、また増えすぎるとコード全体の見通しが悪くなる。

そのため2番目の **{index}`デバッガ<でばっが-デバッガ>`（{index}`debugger`）** を用いたデバッグ実行を行うことが多い。通常のスクリプト実行ではファイル内に記述されたコードを自動的に実行する。これに対しデバッグ実行はスクリプトを自動的に実行するのではなく、「5行目で一時停止して」、「1行だけ実行を進めてまた一時停止して」といった「一時停止」を伴いながら変数を確認することができる。

ターミナルからCUIなデバッガを使うこともできるが、不便なのでGUIなデバッガを提供している実行環境（今回はVS Code）を使おう。

---
## スクリプト例の準備
```python
def play_nabeatsu(input_value):
    if input_value % 3 == 0:
        result = 'アホ'
    else:
        result = input_value
    return result

for i in range(10):
    result = play_nabeatsu(i)
    print(result)
```
VSCodeを起動し、適当な作業用ディレクトリ（例えば ~/prog1/）に week4.py として保存しよう。

---
## VSCodeによる通常実行
まずはスクリプトを通常実行する方法を確認しておこう。以下の方法いずれでも通常実行できる。
- スクリプトファイルを開いている状態で、ウィンドウ右上にある **▷** アイコンをクリックする。
- スクリプトファイルを開いている状態で、「Runメニュー」から **Run without Debugging** を選択する。

コードに誤りがなく、インタプリタが正しく設定されていれば、以下のような出力が得られるはずだ。
```shell
アホ
1
2
アホ
4
5
アホ
7
8
アホ
```

---
## デバッグ実行
デバッグ実行するには以下の2通りの方法がある。
- スクリプトファイルを開いている状態で、ウィンドウ左側にある **虫アイコン付きの▷** をクリックする。
  - デバッグ設定を尋ねられるので、``Python file`` を選択する。
- スクリプトファイルを開いている状態で、「Runメニュー」から **Start Debugging** を選択する。
  - デバッグ設定を尋ねられるので、``Python file`` を選択する。

今の時点では何も設定をしていないため、デバッグ実行をしたとしても最後まで処理を続けて終了してしまう。途中で実行を止めたい場合にはそのための設定（ブレイクポイント）をする必要がある。

---
### ブレイクポイントの設定
実行を一時停止させる場所のことを **{index}`ブレイクポイント<ぶれいくぽいんと-ブレイクポイント>`({index}`breakpoints`)** という。「5行目と11行目で一時停止させたい」のように複数設定することが可能だ。

設定方法は簡単である。**コード中の「行番号の左にある空きスペース」をクリック** すると赤丸が付く。これがブレイクポイントをその行に設定したという意味である。赤丸をクリックするとブレイクポイントを取り消すことができる。なおコメント行や空白行のように、何も実行する命令文がない行にはブレイクポイントを設定することができない。

```{figure} ./figs/debug1.png
:name: debug1
1行目にブレイクポイント設定
```

今回はデバッグ実行の操作自体に慣れることが目的のため、1行目から一時停止させることにしよう。つまり上図のように1行目にブレイクポイントを設定することになる。

---
### デバッグ実行する
```{figure} ./figs/debug2.png
:name: debug2
デバッグ実行1
```

ブレイクポイントを設定した状態でデバッグ実行すると、下記のように変わるはずだ。
- 1行目がハイライトされ、
- 左パネルが **variables, watch, call stack, breakpoints** に変わる。
- ウィンドウ上部に謎のサブメニュー（後述）が出てくる。

左パネルについては、今回は variables だけを眺めていくことにしよう。variablesは変数を意味しており、現在実行中のスクリプトで利用されている変数をここに表示している。実行直後は「1行目がハイライト」されている状態のはずだが、この **ハイライト行は次に実行する行** を示している。まだ1行目は実行していないことに注意しよう。すなわち、まだスクリプトファイルを開いただけの状態である。

```{tip}
スクリプトファイルを開いただけの状態だが、variablesには {index}`special variables` という記載がある。これはスクリプトファイル実行時に自動で設定される変数のことだ。代表的なものに ``__name__`` がある。
```

---
### 実行継続方法の確認
```{figure} ./figs/debug-operator.svg
:name: debug-operator
デバッグメニュー
```

一時停止している状態から実行継続する方法にはいくつかの種類がある。
- {index}`Continue`
  - 次のbreakpointまで実行継続。
- {index}`Step over`
  - 今の行を実行して、次の命令文で停止。
- {index}`Step into`
  - 今の行を実行して、次の命令文で停止。ただし関数呼び出しだった場合、関数の中に移動して停止。
- {index}`Step out`
  - 今いる行が関数の中にある場合、その関数を呼び出している場所まで実行し続けてから停止。
- {index}`Restart`
  - ファイル冒頭からデバッグ実行をやり直す。
- {index}`Stop`
  - デバッグ実行を終了する。

---
### step into 1回目
```{figure} ./figs/debug-stepinto1.png
:name: debug-stepinto1
step into 1回目
```

まずはStep intoに慣れよう。前述の通り step into は「今の行を実行して、次の命令文で停止」する。一度 step into をクリックすると、2行目ではなく8行目に移動して停止する。これは2〜6行目が関数定義であり、実行する命令文ではないためである。また関数宣言を読み込んだ後は、メモリ上に function variables が追加され、その中に play_nabeatsu 関数が保存されている（展開して確認してみよう）。この後は呼び出し実行することができるようになる。これが「関数定義」の意味だ。

---
### step into 2回目
```{figure} ./figs/debug-stepinto2.png
:name: debug-stepinto2
step into 2回目
```

step into 2回目。8行目を実行すると変数iがメモリ上に保存され、その中身が0になっていることが分かる。このことをいちいち printせずとも確認できるのが、冒頭で述べた「デバッガの利点」だ。

---
### step into 3回目
```{figure} ./figs/debug-stepinto3.png
:name: debug-stepinto3
step into 3回目
```

step into 3回目。9行目を実行すると1行目に実行行が移動する。これは9行目が関数呼び出しになっており、その関数定義が1行目から始まっているからだ。この時点ですでに引数 input_value の中身が 0 になっていることが分かる。同時に、この時点で先程メモリ上に記録されていた変数iが消えてしまっていることが分かるだろう。この変数が見える範囲を「スコープ」と呼ぶ。

---
## まとめ
以上が step into の動作である。動作は異なるが step over, step out も同様であり、プログラム実行中の動作を詳細に確認していくことができる。動作確認を行うことで想定外の動作をしている箇所を判断しやすくなり、修正方法の検討に活かしやすくなる。また他人が書いたコードの動作を確認するためにもよく使う。デバッグ実行はプログラミングにおいて極めて重要であるため、今から練習しよう。何かあればデバッグで動作確認しよう。
