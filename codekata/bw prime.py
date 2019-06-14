s1,t1=map(int,input().split())
for x in range(s1+1,t1):
  sum =0
  temp =x
  while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
  if x==sum:
    print(x,end=' ')
