string=str(input())
count=0
for i in string:
  if i.isspace():
    count+=1
print(count)
