number=int(input())
for i in range(number):
  n=list(map(int,input().split()))
  avg=sum(n)//number
  print(avg)
