# 演習3: ブーリアンと文字列処理

## グループ分けをしたい
- 背景
  - 2021年3月現時点ではまだ三密回避が重要である。プログラミング1の受講生はおおよそ60名であり、再履修生も含めると70名程度となることが多い。これに対し教室定員は72名であることから、受講生全員が同時に入室すると三密を回避できない。
  - 教室定員に対し充足率50%にするために、来訪可能な学生を「学籍番号奇数組」「学籍番号偶数組」に分けて指定することにした。
- 作業内容
  - あなたの学籍番号（数字6桁）を入力した時に、あなたが奇数組・偶数組どちらに属するかを出力するプログラムを書け。

`````{admonition} 補足
````{dropdown} 回答例
```python
my_account = 945734
if my_account % 2 == 0:
    print("偶数組")
else:
    print("奇数組")
```
````
`````

---
## 複数のグループに分けたい
- 背景
  - 三密回避のために半分に分けることを考えたが、それではまだ不十分かもしれない。そこで下2桁の数字で「1番〜20番」「21番〜40番」「41番〜60番」「それ以外」の4つのグループに分けて指定することにした。便宜上1つ目をグループ1、2つ目をグループ2、、として名付けることとする。
- 作業内容
  - あなたの学籍番号（数字6桁）を入力した時に、あなたがどのグループに属するかを出力するプログラムを書け。
- ヒント
  - あくまでも入力するのは数字6桁の学籍番号である。ここから下2桁の数字を取り出すにはどうしたら良いだろうか。

`````{admonition} 補足
````{dropdown} 回答例
```python
# 例1
my_account = 945734
target = my_account % 100
if (0 < target) and (target <= 20):
    print("グループ1")
elif (20 < target) and (target <= 40):
    print("グループ2")
elif (40 < target) and (target <= 60):
    print("グループ3")
else:
    print("グループ4")

# 例2
my_account = 945734
target = my_account % 100
if 0 < target:
    if target <= 20:
        print("グループ1")

if 20 < target:
    if target <= 40:
        print("グループ2")

if 40 < target:
    if target <= 60:
        print("グループ3")

if 60 < target:
    print("グループ4")
```
````
`````

---
## 全員を複数のグループに分けたい
- 背景
  - 先程は「あなたの学籍番号に対して所属グループを出力するプログラム」を書いた。これだとその一人のことしか分からなくて不便だ。まとめて一覧表示させたい。
- 作業内容
  - 今年度の受講生は 215701〜215760 だと仮定する。この60人分の所属を出力するプログラムを書け。
  - なお ``make_group(215701, 215760)`` として実行できる関数として記述せよ。

`````{admonition} 補足
```python
#実行イメージ
>>> make_group(215701, 215760)
215701 グループ1
215702 グループ1
215703 グループ1
(略)
215760 グループ3
```

````{dropdown} 回答例
```python
def make_group(begin, end):
    for student_account in range(begin, end+1):
        target = student_account % 100
        if 0 < target <= 20:
            print(student_account, 'グループ1')
        elif 20 < target <= 40:
            print(student_account, 'グループ2')
        elif 40 < target <= 60:
            print(student_account, 'グループ3')
        else:
            print(student_account, 'グループ4')

# 動作確認
make_group(215701, 215760)
```
````
`````

---
## 全員をアカウント名にして複数のグループに分けたい
- 背景
  - 先程は「今年度の受講生60人分の所属グループを出力するプログラム」を書いた。数字のままでは学内で利用しているアカウントとは異なるため不便だ。アカウントに変換したい。
- 作業内容
  - 先程の一覧をアカウントで出力するプログラムを書け。
  - なお ``make_group(215701, 215760)`` として実行できる関数として記述せよ。

`````{admonition} 補足
```python
#実行イメージ
>>> make_group(215701, 215760)
e215701 グループ1
e215702 グループ1
e215703 グループ1
(略)
e215760 グループ3
```

````{dropdown} 回答例
```python
# 例
def make_group(begin, end):
    for student_account in range(begin, end+1):
        target = student_account % 100
        student_account = 'e' + str(student_account)
        if 0 < target <= 20:
            print(student_account, 'グループ1')
        elif 20 < target <= 40:
            print(student_account, 'グループ2')
        elif 40 < target <= 60:
            print(student_account, 'グループ3')
        else:
            print(student_account, 'グループ4')

# 動作確認
make_group(215701, 215760)

```
````
`````
