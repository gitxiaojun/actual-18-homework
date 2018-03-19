#encoding: utf-8
for x in range(1,10):
  for y in range(1,10):
      print(x,'*',y,'=',x*y,'\t',end='')
      if x==y:
        print('')
        break
