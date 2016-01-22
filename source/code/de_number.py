#coding:utf-8
f=open('../lexDic/union/1234')
t=f.read().strip().split('\n')
f.close()
fnum=open('../dxtracted/excluded/number','w')
f=open('../dxtracted/1234','w')
NB = ['一','二','三','四','五','六','七','八','九']
for w in t:
    if w == '一五一十':
        f.write(w+'\n')
        continue
    i = w.find('万')
    if i > 0 and w[i-3:i] in ['十','百','千','亿']:
        fnum.write(w+'\n')
        continue
    isNum = False
    if w[:3] == '第':
        fnum.write(w+'\n')
        isNum = True
    else:
        i = w.find('十')
        if i > 0 and w[i-3:i] in NB[1:]:
            fnum.write(w+'\n')
            isNum = True
        elif i < 9 and w[i+3:i+6] in NB:
            fnum.write(w+'\n')
            isNum = True
        elif i == -1:
            for j in ['百','千','万','亿']:
                k = w.find(j)
                if k > 0 and w[k-3:k] in NB:
                    fnum.write(w+'\n')
                    isNum = True
                    break
    if not isNum:
        f.write(w+'\n')
fnum.close()
f.close()





