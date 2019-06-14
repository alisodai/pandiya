a1=int(input())
x=list(map(int,input().split()))
if (a1==len(x)):
  x.sort()
  for i in x:
    print(i,end=' ')
