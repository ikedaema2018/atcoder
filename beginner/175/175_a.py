str = input()
splited = list(str)
 
cccount = 0
count = 0
for s in splited:
  if s == 'R':
    count = count + 1
    if count > cccount:
      cccount = count
  else:
      count = 0
    
print(cccount)