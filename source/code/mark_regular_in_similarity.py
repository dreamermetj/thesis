#coding:utf-8
f=open('regularSimplified')
t=f.read().decode('utf-8').split('\n')
f.close()
d=dict()
for i in t:
    p=i.split('\t')
    d[p[0]]=p[1]
f=open('../extracted/similarity.txt')
t=f.read().strip().split('\n')
f.close()
f=open('../extracted/similarity1.txt','wb')
for l in t:
    p = l.split('\t')[0].decode('utf-8')
    if (p[0] in d and d[p[0]] == p[1]) or (p[1] in d and d[p[1]] == p[0]):
        f.write('♣\t')
    else:
        f.write('♠\t')
    f.write(l+'\n')
f.close()