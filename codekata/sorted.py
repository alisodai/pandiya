a1=int(input())
x=list(map(int,input().split()))
x.sort()
for i in range(0,a1):
  print(x[i],end=' ')
