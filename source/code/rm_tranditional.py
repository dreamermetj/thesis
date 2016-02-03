#coding:utf-8
f=open('../lexDic/union/1234')
t=f.read().strip().split('\n')
f.close()
f=open('../dxtracted/1234','wb')
exc=open('../dxtracted/excluded/tranditional','wb')
for w in t:
    try:
        w.decode('utf-8').encode('gb2312')
        f.write(w+'\n')
    except:
        exc.write(w+'\n')
f.close()
exc.close()