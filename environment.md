# 全体像, ターミナル, VSCode, Mattermost

## 全体像
- Zoom によるリアルタイムオンライン配信 ＋ 来室による並行実施を予定しています。状況により変わりますので、シラバスやMattermostでの案内を確認ください。
  - **体調不良時には理由を問わず来訪せず、休息かオンライン参加ください。**
- 時間の取れるタイミングでグループ演習（通称モブプログラミング）。
- 大学院生TA（Teaching Assistant）によるサポート。
- オンライン配信は録画しておくので、後日閲覧可能。
- メッセージングアプリ Mattermost による周知、相談対応。
- [モブ・プログラミング](./exercise/howto)
  - コロナ対応のため、実施方法検討中。

---
## 資料のレイアウト
「授業全体」、「Python入門」、「モブプロ演習」、「課題」に分けて資料を配置している。
- 授業全体
  - 環境構築や演習への取り組み方等、特定の週に限定しない共通内容。
- Python入門
  - 毎週の授業資料。
- モブプロ演習
  - モブ・プログラミングで取り組む際の演習。
- 課題
  - 提出が必要な課題レポート。

資料内では Note, Tip 等の強調表示箇所があり、それぞれ以下のように用いている。

```{note}
**Note** は、重要な点を解説している。
```

```{tip}
**Tip** は、その時点における発展的話題を紹介している。
```

```{warning}
**Warning** は、手順を誤るとコンピュータが暴走（無限ループに陥る等）したり、アプリ自体が正しく動作しないといったことに関する注意点を強調している。
```

---
## 開発環境
### 冒頭1〜2週目の環境
- macOS: 12.x以降想定。@ 2022.3.7
  - 恐らく 11.x系でも問題ない。
- ターミナル.app
- Python: 3.9系想定。恐らく3.8系でも問題ない。
- (参考)テキストエディタ: [ATOM](https://atom.io)
  - テキストエディタは他アプリでもOK。テキストエディタが何なのか分からない人はATOMインストールしよう。
- パッケージ管理ツール: conda (miniconda)
  - インストール手順
    - [Mniconda](https://docs.conda.io/en/latest/miniconda.html)からインストール用スクリプトをダウンロード。macOSなら「macOS installers」から選択。
      - Python version: ``Python 3.8``
      - Name: ``Miniconda3 macOS Apple M1 ARM 64-bit bash``
    - ターミナルを起動し、ダウンロードしたスクリプトを実行。以下は実行例。ファイル名は自身がダウンロードしたファイル名に修正すること。
      - ``bash ~/Downloads/Miniconda3-py38_4.10.1-MacOSX-arm64``
      - 途中で何度か質問されるので適切に答えよう。
        - 確認1: In order to continue the installation process, please review the license agreement. Please, press ENTER to continue
          - ENTERキー押そう。
        - 確認2: End User License Agreement - Miniconda
          - ライセンスの中身を確認する画面。問題ないので閉じるために ``q`` を入力しよう。
        - 確認3: Do you accept the license terms? [yes|no]
          - ライセンスを受け入れるかの確認。``yes``
        - 確認4: Miniconda3 will now be installed into this location: /Users/tnal/miniconda3
          - minicondaのインストール先を確認。実行ユーザのホームディレクトリにminiconda3というディレクトリを作成し、そこにインストールするようになっている。このままで良いので、ENTERキーを押そう。
        - 確認5: Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]
          - conda環境初期化を実行することを確認している。``yes``。
        - 確認6: ==> For changes to take effect, close and re-open your current shell. <==
          - conda環境をアクティブにするために、ターミナルを再起動しよう。これでminicondaのインストールが終了。
  - condaに追加パッケージのインストール。
    - ターミナル上で以下を実行。
      - ``conda install numpy matplotlib jupyterlab``
      - 途中で ``Proceed ([y]/n)?`` と確認されるので、``y`` と入力するか、単にEnterキーを押そう。

---
### 2〜3週目以降
- VSCode
  - PDF: <a href="http://ie.u-ryukyu.ac.jp/~tnal/2022/prog1/vscode2022.pdf" target="_blank">VSCodeのインストールから実行まで</a>
  - [デバッグ](./debug)
- 再履修生は PyCharm 等使いたいものを使ってOK。

```{warning}
Applicationsフォルダに置かないと適切に起動できないため、必ずドラッグ＆ドロップで移動してからアプリを起動するようにしよう。
```

---
### 実行環境がない人。
- 手元にまだMacBookがない等、何らかの理由でPython実行環境がない人は、Google Colaboratory と呼ばれる無料のクラウド環境を利用してプログラミングできます。
- 下記URLを Safari 等のブラウザで開く。
  - [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja)
- 右上の「ログイン」から、G-mailアカウント（e2157xx@ie.u-ryukyu.ac.jp）でログイン。
- ファイルメニューから「ノートブックを新規作成」を選択。
  - Untitled0.ipynb という名前のついたファイルが作成される。もし名前を変更したい場合には、拡張子（.ipynb）はそのままにし、その前の「Untilted0」だけを変更しよう。気にしない場合にはそのままでOK。
- 実行してみる。
  - 「右向き矢印」と「灰色背景」の欄があるはず。この欄を「セル」と呼んでおり、このセル内にコードを記述していく。
  - 記述し終えたら「右向き矢印」をクリックするか、Shift + Enter すると、　そのセル内のコードを実行してくれる。
    - 1回目の実行は、環境構築のため時間がかかります。

---
## メッセージングアプリ Mattermost
### チャンネル登録（必須）
授業関連周知はこれを使ってやります。必ず登録してください。

1. Mattermostを起動。
2. チーム「ie-ryukyu」にいることを確認。
3. 「公開チャンネル」の下にある「追加...」をクリック。
  - 検索窓に「prog」と入力。
  - 検索結果に「prog」が出てくるはずなので、それをクリックしてjoin。

---
### Mattermostによる相談の仕方。
- 特に畏まる必要はない。
- 名乗る必要もない。（名乗っても良い）
- 相談内容を prog チャンネルに書き込もう。
  - ＊他人に見られたくない場合には Direct Message でも構いませんが、授業に関係する内容は受講生全員に共通することがほとんどなので、できるだけ prog チャンネルでやり取りしましょう。
