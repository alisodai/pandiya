st1=input()
num=0
for i in range(len(st1)):
  if(st1[i].isdigit() or st1[i].isalpha() or st1[i]==' '):
    continue
  else:
    num=num+1
print(num)  
