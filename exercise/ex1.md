# 演習1: シェルとPythonインタプリタの使用

## 作業用ディレクトリの準備
- 作業内容
  - ターミナルを起動し、今回演習を作業するためのディレクトリとして「~/prog1/ex1/」を作成し、そこに移動せよ。
  - 条件: **本演習はターミナル内で作業すること。**
  - ヒント: プログラミング演習1で習った内容です。
- 補足
  - レポートには、ターミナル上でコマンドを実行した様子と、「~/prog1/ex1/」に移動したことが分かるように、移動後にカレントディレクトリを確認した結果を掲載すること。

`````{admonition} 補足
- Pythonの命令とUnixコマンドとを区別しよう。
- ターミナルを起動した直後はシェルが応答している。シェル上ではUnixコマンド等を指定して実行することができる。
- Unixコマンドと引数は必ずスペースを挟むようにしよう。例えば prog1　ディレクトリに移動するつもりで ``cdprog1`` と書いた場合、コンピュータ（シェル）は「cdprog1というコマンドを実行しろと命令されたけど、そんな命令は知らない」ために実行できず、エラーを返してきます。``cd prog1`` のようにスペースを挿入すると「cdというコマンドにprog1という引数を与えて実行して欲しいんだな」と解釈してくれます。
````{dropdown} 回答例
```shell
# 例1
# まず念の為にホームディレクトリに移動してから実際の作業に取り組んでいる。
# 他ディレクトリに移動していなければ最初のcdは不要。
cd
mkdir prog1
cd prog1
mkdir ex1
cd ex1
pwd

# 例2
# mkdir に -p オプションを付けると、途中階層がなければ自動作成してくれる。
cd
mkdir -p prog1/ex1
cd prog1/ex1
pwd
```
````
`````

---
## 作業用ディレクトリの状態確認
- 作業内容
  - 新規作成した作業用ディレクトリ「~/prog1/ex1/」にはファイルが一つもないはずだ。そのことを確認せよ。
  - 条件: ターミナル内で作業すること。
  - ヒント: プログラミング演習1で既に習った内容です。
- 補足
  - レポートには、ターミナル上でコマンドを実行した様子を掲載すること。

`````{admonition} 補足
- ターミナル上で今作業している対象は何なのかを意識しよう。
- プロンプトが ``>>> `` ならば、今はPythonインタプリタが起動しており、Pythonの命令文だけを実行することができる。
- ターミナルを起動した直後のプロンプト（``username% `` や ``username# ``が多いかな）ならば、今はシェルが起動しており、Unixコマンド等を実行することができる。
````{dropdown} 回答例
```shell
# 例1
ls

# 例2
# -aオプションを付けると隠しファイルも出力される。
# . は「今いるディレクトリ」。
# ..は「今いるディレクトリの親ディレクトリ」。
# どちらもディレクトリ作成した時点で自動生成されるものなので、今回は無視して良い。
ls -a
```
````
`````

---
## Pythonインタプリタを使ってみる
- 作業内容
  - Pythonインタプリタを起動し、 ``print('test')`` を実行してからインタプリタを終了せよ。
- レポートには、下記3点の様子を掲載すること。
  - ターミナル上からPythonインタプリタを起動する様子。
  - インタプリタ上でprint関数を実行する様子。
  - インタプリタを終了して、シェルに戻る様子。

`````{admonition} 補足
- シェルとPythonインタプリタとを行き来する練習。どのモードにいるのかを意識しよう。
````{dropdown} 回答例
```shell
# 例1
python
print('test')
exit()

# 例2
# 3行目の「ctrl-d」は「Ctrolキーを押しながらdを押す」の意。
python
print('test')
ctrl-d
```
````
`````
