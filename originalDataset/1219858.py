#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

input_line = sys.stdin.readline()

n = int(input_line)
S = []

if n==0:
	print("")
	quit()

for i in range(n):
	input_line = sys.stdin.readline()
	S.append(input_line)

used_list = []
used_count = {}
maxLength = 0
for mojiretsu in S:
	_used_dict = {}
	if len(mojiretsu) > maxLength :
		maxLength = len(mojiretsu)
	for moji in mojiretsu:
		if not moji in _used_dict:
			_used_dict[moji] = 0
		if _used_dict[moji] == 0:
			if not moji in used_count:
				used_count[moji] = 0
			used_count[moji] += 1
			_used_dict[moji] = 0
		_used_dict[moji] += 1

	sorted(_used_dict.items(), key=lambda x:x[1], reverse=True)
	used_list.append(_used_dict)

used_flags = []
mojiKeys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

i = 0
candidates = {}
for alpha in mojiKeys:
	if alpha in used_count and used_count[alpha] == n:
		candidates[alpha] = 0
		minimum = maxLength
		for used in used_list:
			if used[alpha] < minimum :
				minimum = used[alpha]
		candidates[alpha] = minimum

output = ""

for i in range(len(mojiKeys)):
	if not mojiKeys[i] in candidates:
		continue
	for j in range(candidates[mojiKeys[i]]):
		output += mojiKeys[i]

print(output)
