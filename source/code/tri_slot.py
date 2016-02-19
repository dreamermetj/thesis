#coding:utf-8
f=open('../extracted/tri_slot/1234_11')
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

f=open('../extracted/tri_slot/explicit_result_11.py','wb')
s = []
for i in d:
    for j in range(4):
        s.append([i.encode('utf-8')+str(j+1),d[i][j]])
s = sorted(s,key=lambda x:x[1],reverse=True)
for p in s:
    f.write(p[0]+'\t'+str(p[1])+'\n')
f.close()

