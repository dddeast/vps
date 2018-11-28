# -*- coding: utf-8 -*-

for line in open("./test/time.db"):
    print line 
    item = line.split(':')
    print item[0]
    print item[1][0:4]+"年"+item[1][4:6]+"月"+item[1][6:8]+"日 " +  item[1][8:10]+":" + item[1][10:]