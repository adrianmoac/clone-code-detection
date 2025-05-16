#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
from bisect import *
from collections import *
import fractions
import heapq 
from itertools import *
import math
import re
import string

N = int(input())
As = list(map(int, input().split()))

four = 0
two = 0
other = 0
for a in As:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1
    else:
        other += 1

prev = 4

def use_other():
    global other, prev
    other -= 1
    prev = 0

def use_two():
    global two, prev
    two -= 1
    prev = 2

def use_four():
    global four, prev
    four -= 1
    prev = 4

def func():
    if prev == 4:
        if other > 0:
            use_other()
        elif two > 0:
            use_two()
        elif four > 0:
            use_four()
    elif prev == 2:
        if two > 0:
            use_two()
        elif four > 0:
            use_four()
        else:
            return False
    elif prev == 0:
        if four > 0:
            use_four()
        else:
            return False
    return True

ok = True
for n in range(N):
    ret = func()
    if not ret:
        ok = False
        break
if ok:
    print("Yes")
else:
    print("No")
