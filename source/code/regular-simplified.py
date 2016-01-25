#coding:utf-8
f=open('regular-simplified.txt')
t=f.read().strip().decode('utf-8').split('\r\n')
f.close()
f=open('regularSimplified','wb')
lnum=len(t)
i=0
c=0
while i < lnum:
    j = i + 1
    print len(t[i])
    print len(t[j])
    for k in range(len(t[i])):
        if t[i][k] != t[j][k]:
            f.write(t[i][k].encode('utf-8')+'\t'+t[j][k].encode('utf-8')+'\n')
        else:
            c+=1
    i += 2
f.close()
print c
