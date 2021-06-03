# -*- coding: utf-8 -*-
'''ドキュメンテーションテスト。
ここにはプログラムファイル全体のドキュメントを書く。
'''

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

if __name__ == "__main__":
    scores = [100, 20, 30]
    for score in scores:
        label = evaluation(score)
        print("{} => {}".format(score,label))
