# 振り返り2

## 振り返り1
- [振り返り1](./summary1)

---
## 文字列・リスト・辞書・集合に対する操作
全ての操作を覚えておく必要はない。代表的な操作（オブジェクトの作成、要素の追加・削除・検索）については身につけておき、必要に応じて調べて使えるようになろう。

---
## ファイル入出力
できる限りwith構文を用い、ファイルハンドラを利用するブロックを限定するように書こう。with構文でブロックを明示することによりcloseし忘れること無く正常にプログラムを終了することができる。

---
## 第三者が利用しやすく、読みやすくする工夫
型ヒント・docstring・doctestを組み合わせることで利用しやすい関数設計を検討しよう。なお、授業の課題で提出するコードは一度書いたらそれで終わりとなることが多いかもしれないが、卒業研究や就職後は **使われ続けるコード** を書くことになる。その際には第三者にとっても読み書きしやすいコードが求められるし、何より自身が書いたコードであっても数週間後には何故そのような実装をしているのか分からなくなってしまうことが珍しくない。もしドキュメント等が全く存在しないなら、バグが見つかった際や新規機能を追加したくなった場合にはその都度全てのコードを読み解かなくてはならず、極めて不合理的だ。「使われ続けるコード」を意識するためにも型ヒント・docstring・doctestを書くようにしよう。

`````{admonition} 検討
下記内容をテキストファイル data.csv として用意し、実行イメージのように処理するコードを検討せよ。
```
id,score
e215780,50
e215781,80
```

```python
>>> # 実行イメージ
>>> filename = 'data.csv'
>>> samples = read_data(filename)
>>> print(len(samples), samples)
2 {'e215780': 50, 'e215781': 80}
```

````{dropdown} 回答例
```python
def read_data(filename: str) -> dict:
    """key,valueの2カラムを保存したCSVファイルを辞書型で読み込む
    Arguments:
      filename (str): 読み込むファイル名。keyはstr型、valueはint型想定。
    Returns:
      data (dict): filenameから読み込んだ辞書型オブジェクト。
    """
    with open(filename, 'r') as f:
        count = 0
        data = {}
        for line in f.readlines():
            if count == 0:
                count += 1
                continue
            items = line.split(',')
            key = items[0]
            value = int(items[1])
            data[key] = value
            count += 1
    return data

filename = 'data.csv'
samples = read_data(filename)
print(len(samples), samples)

```
````
`````
