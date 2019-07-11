str=input()
s=len(str)
count=1
for i in range(s):
  if str[i]=='.':
    count=count+1
print(count)
