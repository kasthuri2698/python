number=int(input())
i=0
first=0
second=1
while(i<number+1):
  if(number<=1):
    next=i
  else:
    next=first+second
    first=second
    second=next
  print(next,end=' ')
  i=i+1
