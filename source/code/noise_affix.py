#coding:utf-8
import json
f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()
f=open('basicWord')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
wd={}
for w in t:
    wd[w] = 0
for mode in ['12','34']:
    f=open('../dxtracted/noiseAffix/'+mode+'.py','wb')
    affix = ''
    cd = {}
    s = sorted(d[mode].iteritems(),key=lambda x:len(x[1]),reverse=True)
    for construction in s:
        if mode == '12':
            affix = construction[0][:2]
        else:
            affix = construction[0][2:]
        count = str(len(construction[1]))
        if count not in cd:
            cd[count] = [0,1]
        else:
            cd[count][1] += 1
        if affix not in wd:
            f.write('#')
            cd[count][0] += 1
        f.write(affix.encode('utf-8')+'\t'+count+'\n')
    f.write('='*16+'\n')
    s = sorted(cd.iteritems(),key=lambda x:int(x[0]),reverse=True)
    for i in s:
        f.write(i[0]+'\t'+str(i[1][0])+' / '+str(i[1][1])+'\n')
    f.close()



