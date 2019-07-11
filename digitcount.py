string=str(input())
count=1
for i in string:
  if i.isdigit():
    count=count+1
print(count)
