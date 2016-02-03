#coding:utf-8
import json, re
f=open('/Users/Dreamer/Desktop/syndict.txt')
t=f.read().strip().split('\n')
f.close()
d=dict()
r=re.compile('[a-z]+[1-5]')
for w in t:
    arr=w.split('\t')
    try:
        py = re.sub('([^e])r(\d)','\g<1>\g<2>er2',arr[3][1:-1])
        py = re.sub('([a-z])er(\d)','\g<1>e\g<2>er2',py)
        py = r.findall(py)
        hz = arr[1][1:-1].decode('utf-8')
        for i in range(len(hz)):
            if hz[i] not in d:
                d[hz[i]] = [py[i]]
            elif py[i] not in d[hz[i]]:
                d[hz[i]].append(py[i])
    except:
        continue

f=open('pinyinJson','w')
f.write(json.dumps(d))
f.close()
print len(d)