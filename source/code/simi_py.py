#coding:utf-8
import json
f=open('pinyinJson')
d=json.loads(f.read())
f.close()
f=open('../extracted/pure_simi.txt')
t=f.read().strip().decode('utf-8').split('\n')
f.close()

for i in range(len(t)):
    if t[i][0] not in d or t[i][1] not in d:
        t[i] = list(t[i]).append(0)
    else:
        py0 = d[t[i][0]]
        py1 = d[t[i][1]]
f=open('../extracted/similarity-pinyin-desc.txt','wb')