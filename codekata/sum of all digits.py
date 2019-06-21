pqr=int(input())
s=0
while(pqr>0):
  r=pqr%10
  s=s+r
  pqr=pqr//10
print(s)
