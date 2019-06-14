b=input()
l1=['a','e','i','o','u','A','E','I','O','U']
if(b.isalpha()):
  if(b in l1):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
