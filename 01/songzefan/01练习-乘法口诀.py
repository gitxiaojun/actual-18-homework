#/usr/bin/env python
# -*- coding: utf-8 -*-
# auth: songzefan
# time: 2018-03-18


i=1
while i<=9:
    j=1
    while j <= i:
        print(str(j) +'*'+ str(i) + '=' + str(i*j),end='\t')
        j+=1
    print()
    i+=1
        
