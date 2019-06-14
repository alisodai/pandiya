s1,t1=map(int,input().split())
for m in range(s1+1,t1):
  if m>1:
    for l in range(2,m):
      if(m%l==0):
        break
    else:
      print(m,end=' ')
