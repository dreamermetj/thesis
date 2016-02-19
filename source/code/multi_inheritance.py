#coding:utf-8
import json
f=open('../lexDic/93050/extracted/json/full_dict')
d=json.loads(f.read())
f.close()

rev = dict()
for mode in d:
    for construction in d[mode]:
        l = len(d[mode][construction])
        for instance in d[mode][construction]:
            if instance not in rev:
                rev[instance] = [[construction, l]]
            else:
                rev[instance].append([construction, l])

f=open('../lexDic/93050/union/1234')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
for w in t:
    if w not in rev:
        rev[w] = []

srev = sorted(rev.iteritems(),key=lambda x:len(x[1]),reverse=True)

f=open('../extracted/multi_inheritance.txt','wb')
for p in srev:
    f.write(p[0].encode('utf-8')+'\t'+str(len(p[1]))+'\t[')
    for i in range(len(p[1])):
        f.write('('+p[1][i][0].encode('utf-8')+','+str(p[1][i][1])+')')
        if i < len(p[1])-1:
            f.write(', ')
    f.write(']\n')
f.close()