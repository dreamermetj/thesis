#coding:utf-8
import json
f = open('../extracted/json/full_dict')
d = json.loads(f.read())
f.close()
simD = dict()
ITER = 21
for mode in ['123','124','134','234']:
    for construction in d[mode]:
        cc = len(d[mode][construction])
        for thes in range(ITER):
            if cc == thes+2:
                index = int((set(['1','2','3','4']) - set(sorted(mode))).pop()) - 1
                for i in range(cc-1):
                    for j in range(i+1,cc):
                        pair = d[mode][construction][i][index] + d[mode][construction][j][index]
                        if pair in simD:
                            simD[pair][thes] += 1
                        elif pair[::-1] in simD:
                            simD[pair[::-1]][thes] += 1
                        else:
                            simD[pair] = [0 for k in range(ITER)]
                            simD[pair][thes] += 1
s = sorted(simD.iteritems(),key=lambda x:sum(x[1]),reverse=True)
f = open('../extracted/similarity/similarity++.txt','wb')
for i in s:
    f.write(i[0].encode('utf-8')+'\t'+str(sum(i[1]))+'\n')

f.close()


