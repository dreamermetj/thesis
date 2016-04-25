#coding:utf-8

f = open('../lexDic/union/1234')
t = f.read().decode('utf-8')
f.close()
lns = t.strip().split('\n')
s = []
for l in lns:
    s.append([''.join(sorted(l)),l])
s = sorted(s, key=lambda x:x[0])
former = ''
same = []
trans = []

def collectTrans():
    if len(same) > 1:
        trans.append(same)

print 'collect transformations ...'
for p in s:
    if p[0] == former:
        same.append(p[1])
    else:
        collectTrans()
        same = [p[1]]
        former = p[0]
collectTrans()

f = open('../extracted/transformation2.txt', 'wb')
total = []
print 'output 数字 ...'
f.write('***********数字：***********\n')
NUMBERS = [
    '一'.decode('utf-8'),
    '二'.decode('utf-8'),
    '三'.decode('utf-8'),
    '四'.decode('utf-8'),
    '五'.decode('utf-8'),
    '六'.decode('utf-8'),
    '七'.decode('utf-8'),
    '八'.decode('utf-8'),
    '九'.decode('utf-8'),
    '十'.decode('utf-8')
]
subtotal=['数字',0]
for i in range(len(trans)):
    if not trans[i]:
        continue
    count = 0
    if trans[i][0][0] == '第'.decode('utf-8') and trans[i][0][1] in NUMBERS:
        f.write(', '.join(trans[i]).encode('utf-8')+'\n')
        trans[i] = []
        subtotal[1] += 1
        continue
    for j in range(4):
        if trans[i][0][j] == '十'.decode('utf-8'):
            if (j > 0 and trans[i][0][j-1] in NUMBERS) or (j < 3 and trans[i][0][j+1] in NUMBERS):
                f.write(', '.join(trans[i]).encode('utf-8')+'\n')
                trans[i] = []
                subtotal[1] += 1
                break
total.append(subtotal)
subtotal=['叠字',0]
print 'output 叠字 ...'
f.write('***********叠字：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = ''.join(sorted(trans[i][0]))
    if fir[0] == fir[1] or fir[1] == fir[2] or fir[2] == fir[3]:
        f.write(trans[i][0].encode('utf-8'))
        f.write(', ')
        f.write(trans[i][1].encode('utf-8'))
        f.write('\n')
        trans[i] = []
        subtotal[1] += 1
total.append(subtotal)
subtotal=['二四交换',0]
print 'output 二四交换 ...'
f.write('***********二四交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[0] == sec[0] and fir[1] == sec[3] and fir[3] == sec[1]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['一三交换',0]
print 'output 一三交换 ...'
f.write('***********一三交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[1] == sec[1] and fir[0] == sec[2] and fir[2] == sec[0]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['三四交换',0]
print 'output 三四交换 ...'
f.write('***********一二不变，三四交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[1] == sec[1] and fir[3] == sec[2] and fir[2] == sec[3]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['一二交换',0]
print 'output 一二交换 ...'
f.write('***********一二交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[2] == sec[2] and fir[0] == sec[1] and fir[1] == sec[0]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['一四交换',0]
print 'output 一四交换 ...'
f.write('***********一四交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[3] == sec[0] and fir[1] == sec[1] and fir[2] == sec[2]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['二三交换',0]
print 'output 二三交换 ...'
f.write('***********二三交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[3] == sec[3] and fir[1] == sec[2] and fir[2] == sec[1]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['前后交换',0]
print 'output 前后交换 ...'
f.write('***********前后交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[1] == sec[3] and fir[0] == sec[2] and fir[3] == sec[1]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['逆序交换',0]
print 'output 逆序交换 ...'
f.write('***********逆序交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[0] == sec[3] and fir[1] == sec[2] and fir[2] == sec[1]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['前后分别交换',0]
print 'output 前后分别交换 ...'
f.write('***********前后分别交换：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    fir = trans[i][0]
    sec = trans[i][1]
    if fir[0] == sec[1] and fir[1] == sec[0] and fir[2] == sec[3]:
        trans[i] = []
        subtotal[1] += 1
        f.write(fir.encode('utf-8'))
        f.write(', ')
        f.write(sec.encode('utf-8'))
        f.write('\n')
total.append(subtotal)
subtotal=['其他二词组',0]
print 'output 其他二词组 ...'
f.write('***********其他二词组：***********\n')
for i in range(len(trans)):
    if not trans[i] or len(trans[i]) > 2:
        continue
    f.write(', '.join(trans[i]).encode('utf-8')+'\n')
    trans[i] = []
    subtotal[1]+=1
total.append(subtotal)
subtotal=['多余二词组',0]
print 'output 多余二词组 ...'
f.write('***********多余二词组：***********\n')
trans = sorted(trans, key=lambda x:len(x))
for i in trans:
    if not i:
        continue
    f.write(', '.join(i).encode('utf-8')+'\n')
    subtotal[1] += 1
total.append(subtotal)
for i in total:
    f.write(i[0]+'\t'+str(i[1])+'\n')
f.close()




