# Numpyを使ったベクトル・行列演算入門

## Numpyのインストール
新入生はインストール大会でインストール済みのはずです。
- 2021年度学生
  - ``source ~/.venv/prog1/bin/activate``
  - ``pip install numpy``
- 2020年度学生
  - ``conda install numpy``

---
## 共通した流れ
- Step1: {index}`Numpy`モジュールを読み込む
- Step2: 演算したいデータ（ベクトルor行列）を{index}`numpy.ndarray型`オブジェクトとして表現する。
- Step3: 演算する。

---
## 具体例: 行列の用意、スカラーと行列の演算、行列同士の足し算、転置、行列積、行列式、逆行列、固有値、固有ベクトル
```python
# 慣例としてnpというエイリアスを付けることが多い。
import numpy as np

# 2行2列の行列を用意。
# 1行を1リストとして列挙し、全体をリストで囲う。
a = np.array([[1., 0.], [0., 2.]])
b = np.array([[1, 2], [3, 4]])

# 変数の中身を確認。
print(a)

# 行列と数値の演算。
# numpy.ndarray型オブジェクトと、int型もしくはfloat型オブジェクトの四則演算をすると、
# 全ての要素に対する四則演算になる。
c = a + 2
print(c)
c = a - 2
print(c)
c = a * 2
print(c)
c = a / 2
print(c)

# 行列同士の足し算。
# これまでに習った「list型」だと、+演算子はリスト同士の結合になるが、
# numpy.ndarray型だと「行列同士の足し算」になる。
c = a + b
print(c)

# 行列の転置。
# numpy.ndarray型オブジェクトに対して「.T」を付けると天地になる。
print(a)
print(a.T)

# 行列同士の積。
# *演算子ではなく、専用の関数 np.dot() を使うことに注意。
# 通常の掛け算と異なり、行列を掛ける順番によって結果も異なる。
c = np.dot(a, b)
print(c)
c = np.dot(b, a)
print(c)

# 行列式を求める。
c = np.linalg.det(a)
print(c)

# 逆行列を求める。
c = np.linalg.inv(a)
print(c)

# 逆行列が正しいか検算してみる。
inv_a = np.linalg.inv(a)
c = np.dot(a, inv_a)
print(c)
c = np.dot(inv_a, a)
print(c)

# 固有値・固有ベクトルを求める。
# np.linalg.eig() 関数で両方を一度に求めることができる。
# 戻り値の1つ目が固有値、2つ目が固有ベクトル。
eigenvalues, eigenvectors = np.linalg.eig(a)
print('固有値: {0}'.format(eigenvalues))
print('固有ベクトル:\n{0}'.format(eigenvectors))
```

---
## よく使う機能: 0行列、1行列、対角行列
- 0行列: ``np.zeros()``
- 1行列: ``np.ones()``
- 対角行列: ``np.eye()``, ``np.diag()``

---
## 参考サイト
- [Numpy公式チュートリアル](https://docs.scipy.org/doc/numpy/user/quickstart.html)
- [私訳「暫定的 NumPy チュートリアル」](http://naoyat.hatenablog.jp/entry/2011/12/29/021414) by naoya_t@hatenablog
