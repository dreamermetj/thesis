#coding:utf-8
import json
f=open('../extracted/json/full_dict')
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

f=open('../lexDic/union/1234')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
for w in t:
    if w not in rev:
        rev[w] = []
'''
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
'''
def stat(thr,fo):
    s=[0]*11
    for i in rev:
        count = 0
        for j in rev[i]:
            if j[1] >= thr:
                count += 1
        s[count] += 1
    fo.write('*** threshold='+str(thr)+' ***\n')
    for i in range(11):
        fo.write(str(i)+': '+str(s[i])+'\n')

f=open('../extracted/multi_inheritance_stat.txt','w')
stat(2,f)
stat(5,f)
stat(10,f)
stat(20,f)
f.close()