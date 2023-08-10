l, r = input().split()
count = 0
flag = True

if ("8" not in l and "8" not in r) or (len(l) != len(r)):
  print(0)
else:
  for l_num, r_num in zip(l, r):
    if l_num == r_num:
      if l_num == "8" and flag:
        count +=1
      else:
        flag = True
    else:
      flag = False
print(count)


