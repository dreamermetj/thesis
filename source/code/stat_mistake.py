#coding: utf-8
import json
f=open('../extracted/json/full_dict_30175')
d=json.loads(f.read())
f.close()
for mode in d:
    if len(mode) > 2:
        continue
    count = 0
    for c in d[mode]:
        if len(d[mode][c]) > 2:
            continue
        l = d[mode][c][0]
        r = d[mode][c][1]
        s = (l[0] == r[0]) + (l[1] == r[1]) + (l[2] == r[2]) + (l[3] == r[3])
        if s == 3:
            count += 1
    print mode + ': ' + str(count)
