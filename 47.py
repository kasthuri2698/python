number=int(input())
for i in range(number):
  num=list(map(int,input().split()))
  x=min(num)
  y=max(num)
  print(x,y)
