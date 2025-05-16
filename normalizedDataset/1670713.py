#-*-coding: utf-8-*-# 切り下げるメソッド
def id0(id1):
    # 0～4は0に
    if 0<=id2(id1[3:4])<=4:
        return id1[0:3]+"0"
    # 5～9は5に
    if 5<=id2(id1[3:4])<=9:
        return id1[0:3]+"5"
 
# 切り上げるメソッド
def id3(id1):
    # 0はそのまま
    if id2(id1[3:4])==0:
        return id1
    # 1～5は5に
    if 1<=id2(id1[3:4])<=5:
        return id1[0:3]+"5"
    # 6～9は0に
    if 6<=id2(id1[3:4])<=9:
        # 50分台だけは時のケタが動く
        if id1[2:3]=="5":
            return id4(id2(id1[0:2])+1)+"00"
        # 通常は10分のケタが動く
        else:
            return id1[0:2]+id4(id2(id1[2:3])+1)+"0"
 
# 入力の数値
id5=id2(input())
id6=[input() for _ in id7(id5)]
 
# 開始時刻と終了時刻のペアで二次元リストを作る
id8=[[0 for id9 in id7(2)] for id10 in id7(id5)]
id11=0
for id12 in id6:
    # 丸め処理を完了させる
    id8[id11][0]=id0(id12[0:4])
    id8[id11][1]=id3(id12[5:9])
    id11+=1
 
# 5分毎の時刻を格納する辞書
id13={}
for id11 in id7(0, 2401, 5):
    id13[id11]=False
 
# 開始終了ペアの数でループ
for id11 in id7(id5):
    id14=id2(id8[id11][0])
    id15=id2(id8[id11][1])
    # 開始時刻から終了時刻までの辞書の値をTrueにする
    for id16 in id7(id14, id15, 5):
        id13[id16]=True
 
# 辞書をキーでソート
id17=id18(id13.id19())
 
# フラグを使って開始終了の境界を判別する
id20=False
for id21, id22 in id17:
    if id22 is True and id20 is False:
        id20=True
        # 桁埋めして文字列に戻す
        id14=id4("%04d"%id21)
    if id22 is False and id20 is True:
        id20=False
        id15=id4("%04d"%id21)
        # 条件に当てはまった開始終了ペアを出力
        print(id14+"-"+id15)