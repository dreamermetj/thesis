#coding:utf-8
import json
f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()
f=open('../dxtracted/excluded/tranditional')
t=f.read().decode('utf-8').strip().split('\n')
f.close()
trans=dict()
for w in t:
    var = []
    c = w
    for p in range(4):
        try:
            w[p].encode('gb2312')
        except:
            c=c[:p]+'…'.decode('utf-8')+(c[p+1:] if p < 3 else '')
            var.append(p+1)
    mode = ''
    for p in range(1,5):
        if p not in var:
            mode += str(p)
    if len(mode) < 2:
        trans[w] = ['too much']
        continue
    if c in d[mode]:
        ins = d[mode][c]
        for i in ins:
            try:
                i.encode('gb2312')
                if w in trans:
                    trans[w].append(i)
                else:
                    trans[w]=[i]
            except:
                continue
    if w not in trans:
        trans[w] = []
s=sorted(trans.iteritems(),key=lambda x:(len(x[1]),x[1]),reverse=True)
f=open('../dxtracted/excluded/validate_tranditional','wb')
for i in s:
    f.write(i[0].encode('utf-8')+'\t\t')
    if len(i[1]) > 5:
        f.write(str(len(i[1]))+'\n')
    else:
        f.write(', '.join(i[1]).encode('utf-8')+'\n')
f.close()
