# -*- coding: UTF-8 -*-
from ctypes import *

libFile = './nlpir/libNLPIR.so'

dll =  CDLL(libFile)
def loadFun(exportName, restype, argtypes):
    global dll
    f = getattr(dll,exportName)
    f.restype = restype
    f.argtypes = argtypes
    return f

class ENCODING:
    GBK_CODE        =   0               #默认支持GBK编码
    UTF8_CODE       =   GBK_CODE+1      #UTF8编码
    BIG5_CODE       =   GBK_CODE+2      #BIG5编码
    GBK_FANTI_CODE  =   GBK_CODE+3      #GBK编码，里面包含繁体字

class POSMap:
    ICT_POS_MAP_SECOND  = 0 #计算所二级标注集
    ICT_POS_MAP_FIRST   = 1 #计算所一级标注集
    PKU_POS_MAP_SECOND  = 2 #北大二级标注集
    PKU_POS_MAP_FIRST   = 3	#北大一级标注集

Init = loadFun('NLPIR_Init',c_int, [c_char_p, c_int, c_char_p])
Exit = loadFun('NLPIR_Exit',c_bool, None)
ParagraphProcess = loadFun('NLPIR_ParagraphProcess',c_char_p, [c_char_p, c_int])

if not Init('',ENCODING.UTF8_CODE,''):
    print("Initialization failed!")
    exit(-111111)
'''
f = open('wordlist.txt', 'rb')
t = f.read()
f.close()
f = open('basicWord', 'w')
for i in t.split('\n'):
    seg = ParagraphProcess(i, c_int(1))
    if len(seg.strip().split(' ')) == 1:
        f.write(i+'\n')
f.close()
'''
t = '…不定'
r = '…左…右'
print ParagraphProcess(t, c_int(1))
print ParagraphProcess(r, c_int(1))










