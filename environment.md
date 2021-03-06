# 全体像, ターミナル, VSCode, Mattermost

## 全体像
- Zoom によるリアルタイムオンライン配信 ＋ 来室による並行実施。
  - **体調不良時には理由を問わず来訪せず、休息かオンライン参加ください。**
- 時間の取れるタイミングでグループ演習（通称モブプログラミング）。
- 大学院生TA（Teaching Assistant）によるサポート。
- オンライン配信は録画しておくので、後日閲覧可能。
- メッセージングアプリ Mattermost による周知、相談対応。
- [モブ・プログラミング](./exercise/howto)
  - コロナ対応のため、実施方法検討中。
- [お便りコーナー](https://docs.google.com/forms/d/e/1FAIpQLScA5N4Or3V-SJH6o0Qvs6M58PnpyhdQWbduiGS46sHJFd7n3w/viewform?usp=sf_link)による相談対応。

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
- macOS: 10.15以降想定。
- ターミナル.app
- Python: 3.8系想定。恐らく3.9系でも問題ない。
- テキストエディタ: [ATOM](https://atom.io)
- パッケージ管理ツール: pip予定
- 設定手順
```shell
which python3 # /usr/bin/python3 想定
python3 -m venv ~/.venv/prog1
source ~/.venv/prog1/bin/activate
which python # ~/.venv/bin/python 想定
pip install --upgrade pip
pip install numpy matplotlib jupyterlab
```

---
### 2〜3週目以降
- VSCode
  - PDF: <a href="http://ie.u-ryukyu.ac.jp/~tnal/2021/prog1/vscode.pdf" target="_blank">VSCodeのインストールから実行まで</a>
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
