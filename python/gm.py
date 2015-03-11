#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#将'Peo sp20070701.mp3' 改名为 'sp20070701_Peo.mp3'

import os
import sys

path = 'E:\\English\\'
os.chdir(path)
fileList = os.listdir(path)
print fileList

confirm = raw_input('Confirm(y|n): ')
if confirm == 'n':
sys.exit()

for fileItem in fileList:
dotIndex = fileItem.rfind('.')
blkIndex = fileItem.rfind(' ')
fileName1 = fileItem[ : blkIndex]
fileName2 = fileItem[blkIndex + 1 : dotIndex]
fileExt = fileItem[dotIndex : ]
if len(fileName1)<4:
newname = fileName2 + '_' + fileName1 + fileExt
os.rename(os.path.join(path,fileItem),os.path.join(path,newname))
print (fileItem + ' => ' + newname)
