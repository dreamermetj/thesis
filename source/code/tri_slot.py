#coding:utf-8
f=open('../lexDic/union/1234')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
d=dict()
for w in t:
    for i in [0,1,2,3]:
        if not w[i] in d:
            d[w[i]] = [0,0,0,0]
        d[w[i]][i] += 1
def signify(a):
    for i in range(4):
        for j in range(i+1,4):
            if max(a[i],a[j]) > min(a[i],a[j])*10:
                return True
    return False
f=open('../extracted/tri_slot/full_result.py','wb')
s = sorted(d.iteritems(),key=lambda x:sum(x[1]),reverse=True)
for p in s:
    if not signify(p[1]):
        f.write('#')
    f.write(p[0].encode('utf-8')+'\t'+str(p[1])+'\n')
f.close()


