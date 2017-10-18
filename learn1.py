#coding=utf-8
f =open('1.txt','w')
f.write('123')
f.write('\n')
f.write('苗华林')
f.close()
with open('1.txt','r') as r:
    print(r.read())
