# -*- coding: utf-8 -*-

x1, y1, r = map(lambda x:int(x), input().split(" "))
x2, y2, x3, y3 = map(lambda x:int(x), input().split(" "))

# 接点の有無
def has_cross_point(t1, t2, s1, s2, s3):

  if s3 < s1:
    minimum = (s3 - s1) ** 2 - r ** 2 + (t2 - t1) ** 2
    if minimum >= 0:
      return False
    maximum = (s2 - s1) ** 2 - r ** 2 + (t2 - t1) ** 2
  elif ((s2 + s3) / 2 <= s1) and s1 <= s3:
    minimum = - r ** 2 + (t2 - t1) ** 2
    if minimum >= 0:
      return False
    maximum = (s2 - s1) ** 2 - r ** 2 + (t2 - t1) ** 2
  elif s2 <= s1 and (s1 <= (s2 + s3) / 2):
    minimum = - r ** 2 + (t2 - t1) ** 2
    if minimum >= 0:
      return False
    maximum = (s3 - s1) ** 2 - r ** 2 + (t2 - t1) ** 2
  elif s1 < s2:
    minimum = (s2 - s1) ** 2 - r ** 2 + (t2 - t1) ** 2
    if minimum >= 0:
      return False
    maximum = (s3 - s1) ** 2 - r ** 2 + (t2 - t1) ** 2

  if minimum < 0 and 0 < maximum:
    return True
  else:
    return False


def judge_with_noncross():
  #接点なし
  if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2:
    # 円の中に四角
    print("YES")
    print("NO")
  elif x2 < x1 and x1 < x3 and y2 < y1 and y1 < y3:
    # 四角の中に円
    print("NO")
    print("YES")
  else:
    # 四角の外に円
    print("YES")
    print("YES")


if x3 < x1 - r or x1 + r < x2 or y3 < y1 - r or y1 + r < y2:
  judge_with_noncross()
#接点あり
elif has_cross_point(x1, x2, y1, y2, y3):
  print("YES")
  print("YES")
elif has_cross_point(y1, y3, x1, x2, x3):
  print("YES")
  print("YES")
elif has_cross_point(x1, x3, y1, y2, y3):
  print("YES")
  print("YES")
elif has_cross_point(y1, y2, x1, x2, x3):
  print("YES")
  print("YES")
# 接点なし
else:
  judge_with_noncross()